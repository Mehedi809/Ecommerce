from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    banner = Banner.objects.all().order_by('ordering')[:2]
    banner1 = Banner.objects.all().order_by('ordering')[2:5]
    womens_clothings = Product.objects.filter(category__name='Womens Clothings')
    mens_clothings = Product.objects.filter(category__name='Mens Clothings')
    health_and_beauty = Product.objects.filter(category__name='Health & Beauty')
    bath_and_body = Product.objects.filter(category__name='Bath & Body')

    context = {
        'banner': banner,
        'banner1': banner1,
        'womens_clothings': womens_clothings,
        'mens_clothings': mens_clothings,
        'health_and_beauty': health_and_beauty,
        'bath_and_body': bath_and_body
    }
    return render(request, 'store/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    related_product = Product.objects.filter(category = product.category).exclude(pk = pk)
    context = {
        'product': product,
        'related_product': related_product
    }
    return render(request, 'store/product_detail.html', context)


def contact(request):
    return render(request, 'store/contact.html')


def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'store/registration.html', context)