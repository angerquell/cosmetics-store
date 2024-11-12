from django.shortcuts import render
from .models import Item
from django.shortcuts import get_object_or_404

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