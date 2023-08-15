from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('board/', views.post_base, name='post_base'),
    path('board/<int:post_id>/', views.post_detail, name='post_detail'),
    path('board/all', views.post_all, name='post_all'),
    path('board/job', views.post_job, name='post_job'),
    path('board/offer', views.post_offer, name='post_offer'),
    path('board/pro', views.post_pro, name='post_pro'),
    path('board/write/', views.write_post, name='write_post'),
    path('board/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('mypage/', views.mypage, name='mypage'),
]
