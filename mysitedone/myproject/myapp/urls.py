from django.urls import path
from . import views
from .views import user_input, display_users



urlpatterns = [
    path('', views.second, name='second'),
    path('products/', views.product, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('index/', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('catalog/', views.product_catalog, name='product_catalog'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('input/', user_input, name='user_input'),
    path('users/', display_users, name='display_users'),
]
