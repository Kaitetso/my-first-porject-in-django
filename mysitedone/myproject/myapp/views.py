from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, PostForm
from .models import Product
from .models import Post
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User


def index(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def contact(request):
    return render(request, 'user_input.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


def product_catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)


    product.views += 1
    product.save()


    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'add_to_cart.html', {'product': product})

def user_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_users')
    else:
        form = UserForm()
    return render(request, 'user_input.html', {'form': form})

def display_users(request):
    users = User.objects.all()
    return render(request, 'display_users.html', {'users': users})







