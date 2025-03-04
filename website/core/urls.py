from django.contrib.auth import views as auth_views
from django.urls import path

from core import views
from . import api_views 
from website import admin_views

urlpatterns = [
    # Trang Landing
    path('', views.landing_page, name='landing_page'),
    
    # Trang chủ (hiển thị tất cả blog)
    path('home/', views.HomePageView.as_view(), name='home'),
    
    # Quản lý Blog (tạo, xem chi tiết, cập nhật, xóa từng bài)
    path('blog/post/', views.BlogCreateView.as_view(), name='post'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete'),
    
    # Quản lý người dùng (Admin)
    path('admin/user-management/', admin_views.user_management, name='user_management'),

    # API
    path('api/like-toggle/', api_views.LikeToggleAPIView.as_view(), name='like-toggle'),
    path('api/blog/<int:blog_id>/comment/', api_views.CommentCreateAPI.as_view(), name='create_comment_api'),

    # Xác thực
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
    # Quản lý blog của người dùng hiện tại (list và xóa nhiều bài)
    path('blog/list/', views.blog_list, name='blog_list'),
    path('blog/delete-multiple/', views.delete_blog_posts, name='delete_blog_posts'),
]

