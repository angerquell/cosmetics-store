from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Cart
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.paginator import Paginator
def index(request):
    item = Item.objects.all()

    page_num = request.GET.get('page', 1)
    paginator = Paginator(item, 4)
    page_obj = paginator.page(page_num)

    return render(request, 'index.html', {'page_obj':page_obj})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        item = Item.objects.filter(name__istartswith=query)
        print(item)
        return render(request, 'index.html', {'page_obj':item })


def detail(request, pk):
    item = get_object_or_404(Item, pk = pk)
    return render(request, 'detail_item.html', {'item':item})


@login_required
def add_cart(request, pk):
    item = get_object_or_404(Item, pk = pk)
    cart, created = Cart.objects.get_or_create(user = request.user, item = item)
    if created == False:
        cart.quantity = F('quantity') + 1 
    else:
        cart.quantity = 1
    cart.save()
    return redirect('home')
    

def remove_cart(request, pk):
    item = get_object_or_404(Item, pk = pk)
    cart = get_object_or_404(Cart, item = item, user = request.user)
    cart.delete()
    return redirect('cart')

@login_required
def cart(request):
    cart = Cart.objects.filter(user = request.user)
    total_items = sum([i.quantity for i in cart])
    total_cost = sum([i.quantity * i.item.cost for i in cart])
    return render(request, 'cart.html', {'items':cart, 'total_items': total_items, 'total_cost':total_cost})