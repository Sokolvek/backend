from models import User, Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
import json
import codecs

def create_user(request):
    user = User(user_id=1, username='john', password='password123', balance=100, email='john@example.com')
    user.save()

def all_users(request):
    users = User.objects.all().values()  # Получаем все записи пользователей в виде словарей
    return JsonResponse(list(users), safe=False)

def add_user(request):
    data = json.loads(codecs.decode(request.body, 'unicode_escape'))
    
    email = data['email']
    
    # Проверка наличия пользователя с указанным email
    if User.objects.filter(email=email).exists():
        return JsonResponse({'message': 'User with this email already exists'})
    
    user = User.objects.create(username=data['username'], password=data['password'], balance=0, email=email)
    return JsonResponse({'message': 'User created successfully'})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=400)
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
    
