from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ['title','body']
        fields = '__all__'
        exclude = ['author','slug']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
