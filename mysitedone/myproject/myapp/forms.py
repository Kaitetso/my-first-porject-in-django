from django import forms
from .models import Product
from .models import Post
from .models import User



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'comment']
