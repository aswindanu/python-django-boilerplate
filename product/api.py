from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions, status, authentication, viewsets
from account.models import User, AbstractUser
from product.metadata import StandardResultsSetPagination, LargeResultsSetPagination
from product.models import Product
from product.serializers import UserSerializer, ProductSerializer, ProductSerializerAPIView, ProductSerializerGeneric


class ProductListGeneric(generics.ListCreateAPIView):
    """
    List all products, or create a new product.
    Note : Recommended (best practice using generic API)

    List of using generic:
    - CreateAPIView: It provides a  post method handler and it is used for create-only endpoints. CreateAPIView extends GenericAPIView and CreateModelMixin
    - ListAPIView: It provides a get method handler and is used for read-only endpoints to represent a collection of model instances. ListAPIView extends GenericAPIView and ListModelMixin.
    - RetrieveAPIView: It provides a get method handler and is used for read-only endpoints to represent a single model instance. RetrieveAPIView extends GenericAPIView and RetrieveModelMixin.
    - DestroyAPIView: It provides a delete method handler and is used for delete-only endpoints for a single model instance. DestroyAPIView extends GenericAPIView and DestroyModelMixin.
    - UpdateAPIView: It provides put and patch method handlers and is used for update-only endpoints for a single model instance. UpdateAPIView extends GenericAPIView and UpdateModelMixin.

    - ListCreateAPIView: It provides get and post method handlers and is used for read-write endpoints to represent a collection of model instances. ListCreateAPIView extends GenericAPIView, ListModelMixin, and CreateModelMixin..
    - RetrieveUpdateAPIView: It provides get, put, and patch method handlers. It is used to read or update endpoints to represent a single model instance. RetrieveUpdateAPIView extends GenericAPIView, RetrieveModelMixin, and UpdateModelMixin.
    - RetrieveDestroyAPIView: It provides get and delete method handlers and it is used for read or delete endpoints to represent a single model instance. RetrieveDestroyAPIView extends GenericAPIView, RetrieveModelMixin, and DestroyModelMixin.
    - RetrieveUpdateDestroyAPIView: It provides get, put, patch, and delete method handlers. It is used for read-write-delete endpoints to represent a single model instance. It extends GenericAPIView, RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin.

    see docs at
    https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

    i.e.
    https://medium.com/analytics-vidhya/django-rest-framework-views-generic-views-viewsets-simplified-ff997ea3205f
    https://juliensalinas.com/en/django-rest-framework-generic-views/
    https://www.valentinog.com/blog/drf-request/
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializerGeneric
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, put, patch, or delete a product.
    Note : Recommended (best practice using generic API)

    List of using generic:
    - CreateAPIView: It provides a  post method handler and it is used for create-only endpoints. CreateAPIView extends GenericAPIView and CreateModelMixin
    - ListAPIView: It provides a get method handler and is used for read-only endpoints to represent a collection of model instances. ListAPIView extends GenericAPIView and ListModelMixin.
    - RetrieveAPIView: It provides a get method handler and is used for read-only endpoints to represent a single model instance. RetrieveAPIView extends GenericAPIView and RetrieveModelMixin.
    - DestroyAPIView: It provides a delete method handler and is used for delete-only endpoints for a single model instance. DestroyAPIView extends GenericAPIView and DestroyModelMixin.
    - UpdateAPIView: It provides put and patch method handlers and is used for update-only endpoints for a single model instance. UpdateAPIView extends GenericAPIView and UpdateModelMixin.

    - ListCreateAPIView: It provides get and post method handlers and is used for read-write endpoints to represent a collection of model instances. ListCreateAPIView extends GenericAPIView, ListModelMixin, and CreateModelMixin..
    - RetrieveUpdateAPIView: It provides get, put, and patch method handlers. It is used to read or update endpoints to represent a single model instance. RetrieveUpdateAPIView extends GenericAPIView, RetrieveModelMixin, and UpdateModelMixin.
    - RetrieveDestroyAPIView: It provides get and delete method handlers and it is used for read or delete endpoints to represent a single model instance. RetrieveDestroyAPIView extends GenericAPIView, RetrieveModelMixin, and DestroyModelMixin.
    - RetrieveUpdateDestroyAPIView: It provides get, put, patch, and delete method handlers. It is used for read-write-delete endpoints to represent a single model instance. It extends GenericAPIView, RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin.

    see docs at
    https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

    i.e.
    https://medium.com/analytics-vidhya/django-rest-framework-views-generic-views-viewsets-simplified-ff997ea3205f
    https://juliensalinas.com/en/django-rest-framework-generic-views/
    https://www.valentinog.com/blog/drf-request/
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializerGeneric
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
  
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
  
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
  
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
class UserListGeneric(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    Note : Recommended (best practice using generic API)

    List of using generic:
    - CreateAPIView: It provides a  post method handler and it is used for create-only endpoints. CreateAPIView extends GenericAPIView and CreateModelMixin
    - ListAPIView: It provides a get method handler and is used for read-only endpoints to represent a collection of model instances. ListAPIView extends GenericAPIView and ListModelMixin.
    - RetrieveAPIView: It provides a get method handler and is used for read-only endpoints to represent a single model instance. RetrieveAPIView extends GenericAPIView and RetrieveModelMixin.
    - DestroyAPIView: It provides a delete method handler and is used for delete-only endpoints for a single model instance. DestroyAPIView extends GenericAPIView and DestroyModelMixin.
    - UpdateAPIView: It provides put and patch method handlers and is used for update-only endpoints for a single model instance. UpdateAPIView extends GenericAPIView and UpdateModelMixin.

    - ListCreateAPIView: It provides get and post method handlers and is used for read-write endpoints to represent a collection of model instances. ListCreateAPIView extends GenericAPIView, ListModelMixin, and CreateModelMixin..
    - RetrieveUpdateAPIView: It provides get, put, and patch method handlers. It is used to read or update endpoints to represent a single model instance. RetrieveUpdateAPIView extends GenericAPIView, RetrieveModelMixin, and UpdateModelMixin.
    - RetrieveDestroyAPIView: It provides get and delete method handlers and it is used for read or delete endpoints to represent a single model instance. RetrieveDestroyAPIView extends GenericAPIView, RetrieveModelMixin, and DestroyModelMixin.
    - RetrieveUpdateDestroyAPIView: It provides get, put, patch, and delete method handlers. It is used for read-write-delete endpoints to represent a single model instance. It extends GenericAPIView, RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin.

    see docs at
    https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

    i.e.
    https://medium.com/analytics-vidhya/django-rest-framework-views-generic-views-viewsets-simplified-ff997ea3205f
    https://juliensalinas.com/en/django-rest-framework-generic-views/
    https://www.valentinog.com/blog/drf-request/
    """
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializerGeneric
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        for key, val in request.data.items():
            _exception_title = ["username", "password", "email"]
            if key not in _exception_title:
                request.data[key] = val.strip().title()
            else:
                request.data[key] = val.strip()
        return self.create(request, *args, **kwargs)


class ProductListMixins(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    """
    List all products or create a new product.

    List of using mixins:
    - ListModelMixin : list (GET /products/)- list some/all products
    - CreateModelMixin : create(POST /products/) - add a new product

    see docs at
    https://www.django-rest-framework.org/api-guide/generic-views/#mixins

    i.e.
    https://www.geeksforgeeks.org/class-based-views-django-rest-framework/
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializerGeneric
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailMixins(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    """
    Retrieve, put, patch, or delete a product.

    List of using mixins:
    - RetrieveModelMixin : retrieve (GET /products/{pk}) - get a particular product
    - UpdateModelMixin : 
        a. update (PUT /products/{pk}) - update a particular product
        b. partial_update(PATCH /products/{pk}) - update (without validating all fields) a particular product
    - DestroyModelMixin : destroy (DELETE /products/{pk}) - delete a particular product
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializerGeneric
    pagination_class = LargeResultsSetPagination
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
  
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
  
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
  
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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


class ProductAPIView(APIView):
    """
    List all products, or create a new product.
    Note : Better to use generic instead of APIView
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
        serializer = ProductSerializerAPIView(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializerAPIView(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
