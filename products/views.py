from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products':products})

def root(request):
    return redirect('home')

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
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})

    return render(request, 'products/create.html')

@login_required
def remove(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.DoesNotExist:
        return redirect('home')
    else:
        pass
    return render(request, 'products/remove.html')


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context={
        'product': product
    }
    return render(request, 'products/details.html', context)

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes += 1
        product.save()
        return redirect('/products/' + str(product_id))

