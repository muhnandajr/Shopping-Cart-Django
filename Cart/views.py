from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Cart.models import Cart
from Cart.serializers import CartSerializer
from rest_framework.decorators import api_view

from rest_framework import viewsets
from django.db.models import Avg, Max, Min, Sum



@api_view(['GET','POST','DELETE'])
def cart_list(request):
    # GET list of topics, POST a new topic, DELETE all topics
    if request.method == 'GET':
        carts = Cart.objects.all()
        total = Cart.objects.all().aggregate(Sum('quantity'))
        print(total)
        qty = 1
        
        product_id = request.GET.get('product_id', None)
        if product_id is not None:
            carts = carts.filter(product_id__icontains=product_id)
        
        carts_serializer = CartSerializer(carts, many=True)
        return JsonResponse(carts_serializer.data, safe=False)

    elif request.method == 'POST':
            cart_data = JSONParser().parse(request)
            cart_serializer = CartSerializer(data=cart_data)
            if cart_serializer.is_valid():
                cart_serializer.save()
                return JsonResponse(cart_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
            count = Cart.objects.all().delete()
            return JsonResponse({'message': '{} Cart were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) 
    return JsonResponse(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, pk):
    # find topic by pk (id)
    try: 
        cart = Cart.objects.get(pk=pk) 
        if request.method == 'GET':
            cart_serializer = CartSerializer(cart) 
            return JsonResponse(cart_serializer.data)
        elif request.method == 'PUT': 
            cart_data = JSONParser().parse(request) 
            cart_serializer = CartSerializer(cart, data=cart_data) 
            if cart_serializer.is_valid(): 
                cart_serializer.save() 
                return JsonResponse(cart_serializer.data) 
            return JsonResponse(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            cart.delete() 
        return JsonResponse({'message': 'Cart was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Cart.DoesNotExist: 
        return JsonResponse({'message': 'The Cart does not exist'}, status=status.HTTP_404_NOT_FOUND) 

