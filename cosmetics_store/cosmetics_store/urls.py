
from django.contrib import admin
from django.urls import path
from core.views import index, search, detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('search/', search, name = 'search'),
    path('detail/<int:pk>', detail, name = 'detail'),
]
