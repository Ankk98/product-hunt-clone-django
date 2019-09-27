from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.

def home(request):
    context={
        
    }
    return render(request, 'products/home.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['product_name'] and request.POST['description'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['product_name']
            product.description = request.POST['description']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('http://'):
                product.url = request.POST['url']
            else:
                product.url = 'https://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.publishing_date = timezone.datetime.now()
            product.author = request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})

    return render(request, 'products/create.html')

@login_required
def remove(request):
    context={
        
    }
    return render(request, 'products/remove.html', context)


def details(request):
    context={
        
    }
    return render(request, 'products/details.html', context)

