from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    ID = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디'}))
    PWD = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))
    
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")