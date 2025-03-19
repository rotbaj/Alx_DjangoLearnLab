from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView 

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('posts/', views.posts, name='posts'),
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]