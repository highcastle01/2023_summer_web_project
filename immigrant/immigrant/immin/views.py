from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from braces.views import LoginRequiredMixin
from .models import Post, User
from .forms import PostForm
from django.contrib.auth import logout
from django.http import JsonResponse

# from .models import Post

#LoginRequiredMixin
def main(request):
    return render(request, 'immin/main.html')

def chatbot(request):
    return render(request, 'immin/chatbot.html')

def post_base(request):
    posts = Post.objects.all()
    context = {"posts" : posts}
    return render(request, 'immin/post_base.html', context)

def post_all(request):
    return render(request, 'immin/post_all.html')

def post_job(request):
    return render(request, 'immin/post_job.html')

def post_offer(request):
    return render(request, 'immin/post_offer.html')

def post_pro(request):
    return render(request, 'immin/post_pro.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post.view_rating += 1
    post.save()
    context = {"post" : post, "post_id" : post_id}
    return render(request, 'immin/post_detail.html', context)

def write_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # 이미지 업로드를 위해 request.FILES 추가
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            return redirect('post_base')
    else:
        form = PostForm()
    return render(request, 'immin/write_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            return redirect('post_base')
    else:
        form = PostForm(instance=post)

    return render(request, 'immin/edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        if post.author == request.user:
            post.delete()
        return redirect('post_list')

def mypage(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    date_joined = user.date_joined
    context = {
        'date_joined': date_joined,
        'posts': posts,
    }
    return render(request, 'immin/mypage.html', context=context)

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('main')