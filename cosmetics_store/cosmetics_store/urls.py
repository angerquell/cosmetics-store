
from django.contrib import admin
from django.urls import path
from core.views import index, search, detail, add_cart, remove_cart , cart
from django.conf import settings
from django.conf.urls.static import static
from User.views import login_account, logout_account, register_account
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('search/', search, name = 'search'),
    path('detail/<int:pk>', detail, name = 'detail'),
    path('login/', login_account, name = 'login'),
    path('logout/', logout_account, name = 'logout'),
    path('register/', register_account, name = 'register'),
    path('add_cart/<int:pk>', add_cart, name = 'add_cart'),
    path('cart', cart, name = "cart"),
    path('remove_cart/<int:pk>/', remove_cart, name = 'remove_cart'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)