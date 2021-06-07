from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import Product
from .serializers import UserSerializer, ProductSerializer, ProductSerializerAPIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]



class ProductList(APIView):
    """
    List all products, or create a new product.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializerAPIView(products, many=True)

        page = 1
        per_page = 10

        try:
            page = request.GET.get["page"]
        except:
            pass

        try:
            per_page = request.GET["per_page"]
        except:
            pass

        first_page = 1
        total_count = products.count()
        page_count = int(total_count / per_page) + 1 if total_count / per_page > int(total_count / per_page) else int(total_count / per_page)
        last_page = page_count

        context = {}
        context["metadata"] = {}
        context["metadata"]["page"] = page
        context["metadata"]["per_page"] = per_page
        context["metadata"]["first_page"] = first_page
        context["metadata"]["last_page"] = last_page
        context["metadata"]["page_count"] = page_count
        context["metadata"]["total_count"] = total_count
    
        context["products"] = serializer.data
        return Response(context)

    def post(self, request, format=None):
        serializer = ProductSerializerAPIView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)