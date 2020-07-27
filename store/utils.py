import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
        print('cart:', cart)
    except:
        cart = {}
    items = []
    order = {'get_cart_item': 0, 'get_cart_total': 0, 'shipping': False}
    cartItems = order['get_cart_item']
    for i in cart:
        try:

            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = product.price * cart[i]['quantity']
            order['get_cart_total'] += total
            order['get_cart_item'] += cart[i]['quantity']

            item = {
                "product": {
                    "id": product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
            if not product.digital:
                order['shipping'] = True
        except:
            pass
    return {'items': items, 'order': order, 'cartItems': cartItems}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(f'customer{customer}')
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(f'order{order}')
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
        print(f'items{items}')
    else:
        cookidata = cookieCart(request)
        cartItems = cookidata['cartItems']
        order = cookidata['order']
        items = cookidata['items']
    return {'items': items, 'order': order, 'cartItems': cartItems}