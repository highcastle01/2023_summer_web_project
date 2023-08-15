from django import forms
from .models import User, Post

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()

class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea)
    image = forms.ImageField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image1', 'image2', 'image3']