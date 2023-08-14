from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserForm
# from .models import Post

def main(request):
    return render(request, 'immin/main.html')

def chatbot(request):
    return render(request, 'immin/chatbot.html')

def post_base(request):
    # login_session = request.session.get('login_session', '')
    # context = {'login_session' : login_session}
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

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('immin/main.html')  # 로그인 후 리다이렉트할 URL
    else:
        form = LoginForm()
        return render(request, 'immin/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('immin/main.html')
    else:
        form = UserForm()
    return render(request, 'immin/signup.html', {'form': form})

#구인구직게시판
# def post_base(request):
#     posts = Post.objects.all()
#     context = {'posts' : posts}
#     return render(request, 'post_base.html', context)

# def post_detail(request, post_id):
#     post = Post.objects.get(id=post_id)
#     context = {'post' : post}
#     return render(request, 'post_detail.html', context)