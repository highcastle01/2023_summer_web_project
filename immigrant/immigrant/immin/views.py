from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from braces.views import LoginRequiredMixin
# from .models import Post

#LoginRequiredMixin
def main(request):
    return render(request, 'immin/main.html')

def chatbot(request):
    return render(request, 'immin/chatbot.html')

def post_base(request):
    return render(request, 'immin/post_base.html')

def post_all(request):
    return render(request, 'immin/post_all.html')

def post_job(request):
    return render(request, 'immin/post_job.html')

def post_offer(request):
    return render(request, 'immin/post_offer.html')

def post_pro(request):
    return render(request, 'immin/post_pro.html')

def mypage(request):
    return render(request, 'immin/mypage.html')

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('main')