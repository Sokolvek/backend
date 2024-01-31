from models import User, Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms

import json
import codecs

def create_user(request):
    user = User(user_id=1, username='john', password='password123', balance=100, email='john@example.com')
    user.save()

def all_users(request):
    users = User.objects.all().values()  # Получаем все записи пользователей в виде словарей
    return JsonResponse(list(users), safe=False)


class CreationForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["id", "balance"]
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["id", "balance", "email"]

def register_view(request):
    if request.method == 'POST':
        print("its kinda post")
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Registration successful. You can now log in.')
        # return render(request, 'login.html')
    else:
        form = CreationForm()
    return render(request, 'register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.data.get("username"),form.data.get("password"))
        user = authenticate(request, username=form.data.get("username"), password=form.data.get("password"))
        print(user)
        if user is not None:
            login(request, user)
            print("auth")
            # return redirect('home')
        # else:
            
        
            # messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})
    
def update_user(request, user_id):
    user = get_object_or_404(User, user_id=user_id)

    if request.method == 'POST':
        body = json.loads(request.body)
        new_username = body.get('username')
        new_balance = body.get('balance')

        if new_username is not None:
            user.username = new_username
        if new_balance is not None:
            user.balance = new_balance

        user.save()

        return JsonResponse({'message': 'User updated successfully'})

    return JsonResponse({'message': 'error?'})

def delete_user(request, user_id):
    user = get_object_or_404(User, user_id=user_id)

    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})

    return JsonResponse({'message': 'error?'})

def get_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def add_product(request):
    data = json.loads(request.body)
    product = Product.objects.create(product_name=data['product_name'], product_description=data['product_description'], price=data['price'])
    return JsonResponse({'message': 'User created successfully'})

def update_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    body = json.loads(request.body)
    new_product_name = body.get('product_name')
    new_product_description = body.get('product_description')
    product.product_name = new_product_name
    product.product_description = new_product_description
    product.save()
    return JsonResponse({'message':'product updated'})

def delete_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    
    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message':'product deleted'})
    
