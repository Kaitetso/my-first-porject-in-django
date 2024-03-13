import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Product

def populate():
    product1 = Product(name='Продукт 1', price=10.99, description='Описание продукта 1')
    product2 = Product(name='Продукт 2', price=15.49, description='Описание продукта 2')
    product3 = Product(name='Продукт 3', price=20.00, description='Описание продукта 3')

    product1.save()
    product2.save()
    product3.save()

if __name__ == '__main__':
    populate()
