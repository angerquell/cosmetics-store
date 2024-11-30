from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Cart, Category
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



def filter_item(request,category ):
    item = Item.objects.filter(category__name = category)
    catalog = Category.objects.all()
    return render(request, 'index1.html', {'page_obj':item, "catalog":catalog})

class Home(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'catalog'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        item = Item.objects.filter(name__istartswith=query)
        print(request.GET.get('catalog', ''))
        return render(request, 'index1.html', {'page_obj':item })


class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail_item.html'  
    context_object_name = 'item'       

    
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
    
@login_required
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