from .serializers import CategorySerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from .models import Category,Product
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer

class CategoryApiView:

    @api_view(['GET'])
    def categoryList(request):
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    @api_view(['GET'])
    def categoryDetail(request,pk):
        categories=Category.objects.get(id=pk)
        serializer=CategorySerializer(categories,many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def categoryCreate(request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['PUT'])
    def categoryUpdate(request,pk):
        categories=Category.objects.get(pk=pk)
        serializer=CategorySerializer(instance=categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def categoryDelete(request,pk):
        category=Category.objects.get(pk=pk)
        category.delete()

        return Response('deleted')


class ProductApiView:
    @api_view(['GET'])
    def productList(request):
        product=Product.objects.all()
        serializer=ProductSerializer(product,many=True)
        return Response(serializer.data)
    @api_view(['GET'])
    def productDetail(request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product,many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def productCreate(request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['PUT'])
    def productUpdate(request,pk):
        product=Product.objects.get(pk=pk)
        serializer=ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def productDelete(request,pk):
        product=Product.objects.get(pk=pk)
        product.delete()

        return Response('deleted')

    





