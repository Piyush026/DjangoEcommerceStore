from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse
import json


# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(f'customer{customer}')
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(f'order{order}')
        items = order.orderitem_set.all()
        print(f'items{items}')
    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(f'customer{customer}')
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(f'order{order}')
        items = order.orderitem_set.all()
        print(f'items{items}')
    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(f'action {action} and productId {productId}')
    customer = request.user.customer
    return JsonResponse("Item Added", safe=False)
