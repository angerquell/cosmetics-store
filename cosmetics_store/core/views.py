from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Cart
from django.contrib.auth.decorators import login_required

def index(request):
    item = Item.objects.all()
    return render(request, 'index.html', {'items':item})


def search(reqeust):
    if reqeust.method == 'GET':
        query = reqeust.GET.get('q', '')
        item = Item.objects.filter(name__istartswith=query)
        return render(reqeust, 'index.html', {'items':item})


def detail(request, pk):
    item = get_object_or_404(Item, pk = pk)
    return render(request, 'detail_item.html', {'item':item})

@login_required
def add_cart(request, pk):
    item = get_object_or_404(Item, pk = pk)
    cart, created = Cart.objects.get_or_create(user = request.user, item = item)
    if created == False:
        cart.quantity +=1
    else:
        cart.quantity = 1
    cart.save()
    return redirect('home')
    

def remove_cart(request, pk):
    item = get_object_or_404(Item, pk = pk)
    cart = get_object_or_404(Cart, item = item, user = request.user)
    cart.delete()
    return redirect('cart')


def cart(request):
    cart = Cart.objects.filter(user = request.user)
    return render(request, 'cart.html', {'items':cart})