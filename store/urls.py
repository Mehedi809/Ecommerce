from django.contrib import admin
from django.urls import path
from . import views
from . import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('contact', views.contact, name = 'contact'),
    path('product_detail/<pk>', views.product_detail, name = 'product_detail'),
    path('registration', user_views.registration, name = 'registration'),
]
