from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, generics, authentication
from account.models import User
from .metadata import StandardResultsSetPagination, LargeResultsSetPagination
from .models import Product
from .serializers import UserSerializer, ProductSerializer, ProductSerializerAPIView, ProductSerializerGeneric


class ProductListView(generics.ListAPIView):
    """
    List all products, or create a new product.
    Note : Recommended (best practice using generic API)
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializerGeneric
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()

    def get_queryset(self):
        qs = Product.objects.all()
        return qs


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination


class ProductList(APIView):
    """
    List all products, or create a new product.
    """
    authentication_classes = [authentication.TokenAuthentication]
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

    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializerAPIView(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
