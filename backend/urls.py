"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # user
    path('users/', views.all_users, name='all_users'),
    path('register/', views.register_view, name="register_user"),
    path('login/', views.login_view),
    # path('add-users/', views.add_user, name='add_user'),
    path('user/<int:user_id>/', views.update_user, name='update_user'),
    path('user-delete/<int:user_id>/', views.delete_user, name='delete_user'),
    # product
    path('products/', views.get_products, name='get_products'),
    path('add-product/', views.add_product, name='add_product'),
    path('product-update/<int:product_id>', views.update_product, name='update_product'),
    path('product-delete/<int:product_id>', views.delete_product, name='delete_product')
    
]
