from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList, name='post-list'),
    path('post/<int:pk>/', views.PostView, name='post-view'),
    path('post/create/', views.PostCreate, name='post-create'),
    path('post/update/<int:pk>/', views.PostUpdate, name='post-update'),
    path('post/delete/<int:pk>/', views.PostDelete, name='post-delete'),

    path('posts-list-create/', views.PostListCreate, name='post-list-create'),
    path('post-detail/<int:pk>/', views.PostDetail, name='post-detail'),
]