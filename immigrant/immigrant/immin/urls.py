from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('board/', views.post_base, name='post_base'),
    path('board/all', views.post_all, name='post_all'), #<int:pk>넣어야..
    path('board/job', views.post_job, name='post_job'), #<int:pk>넣어야..
    path('board/offer', views.post_offer, name='post_offer'), #<int:pk>넣어야..
    path('board/pro', views.post_pro, name='post_pro'), #<int:pk>넣어야..
    path('login/', auth_views.LoginView.as_view(template_name='immin/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
]
