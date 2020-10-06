from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Product
from main.serializers import ProductSerializer


@api_view(['GET'])
def cart_list(request):
    return Response({'cart': request.session.get('cart')})


@api_view(['POST'])
def add_to_cart(request, pk):

    if 'cart' not in request.session:
        request.session['cart'] = {}
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, context={'request': request})
    if str(pk) not in request.session['cart']:
        request.session['cart'][str(pk)] = 0

    request.session['cart'][str(pk)] += 1

    request.session.modified = True
    return Response({'data': serializer.data, 'cart': request.session['cart']})


@api_view(['DELETE'])
def delete_from_cart(request, pk):
    if 'cart' in request.session:
        if str(pk) in request.session['cart']:
            del request.session['cart'][str(pk)]
            request.session.modified = True
    return Response('Успешно удалено')


@api_view(['DELETE'])
def delete_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
