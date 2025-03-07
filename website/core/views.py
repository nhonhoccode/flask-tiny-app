from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.db.models import Count
from django.db.models import Q
from django.views import View

from .forms import CustomUserCreationForm, CommentForm
from .models import BlogModel, SiteConfiguration

from django.shortcuts import render
from .forms import CustomUserCreationForm
def landing_page(request):
    """Hiển thị trang Landing Page"""
    return render(request, 'core/landing.html')

class LoginView(auth_views.LoginView):
    template_name = 'core/form.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['form_title'] = 'Login'
        context['form_btn'] = 'Login'
        return context
    

class RegisterView(View):
    template_name = 'core/form.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {
            'form': form,
            'form_title': 'Register',
            'form_btn': 'Register',
            'title': 'Register'
        })

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {
            'form': form,
            'form_title': 'Register',
            'form_btn': 'Register',
            'title': 'Register'
        })


class HomePageView(ListView):
    model = BlogModel
    template_name = 'core/index.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        sorted_by = self.request.GET.get('sorted_by')

        # Start with the default queryset
        queryset = BlogModel.objects.all()

        # Filter the blogs based on title, content, or author if there's a search query
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query) |
                Q(author__username__icontains=search_query) |
                Q(author__first_name__icontains=search_query) |
                Q(author__last_name__icontains=search_query)
            )

        # Set the blog order
        ordering = ['-created_at', '-views']
        if sorted_by == 'views':
            ordering = ['-views']
        elif sorted_by == 'likes':
            queryset = queryset.annotate(likes_count=Count('likemodel')).order_by('-likes_count', '-views')

        # Apply the final ordering to the queryset
        if not sorted_by == 'likes':
            queryset = queryset.order_by(*ordering)

        return queryset
    
    def get_paginate_by(self, queryset):
        config = SiteConfiguration.objects.first()
        if config and config.paginate_by:
            return config.paginate_by
        return self.paginate_by


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'core/blog_detail.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        # Get the blog object
        blog = self.get_object()

        # Increment the views count by 1
        blog.views += 1
        blog.save()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        context['comment_form'] = CommentForm()
        return context


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BlogModel
    template_name = 'core/form.html'
    fields = ['title', 'content', 'media']
    success_message = 'The blog post was successfully posted.'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Make Blog'
        context['form_title'] = 'Make Blog'
        context['form_btn'] = 'Post'
        context['with_media'] = True
        return context
    

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = BlogModel
    template_name = 'core/form.html'
    fields = ['title', 'content', 'media']
    success_message = 'The blog post was successfully updated.'

    def test_func(self):
        # Check if the authenticated user is the author of the blog
        return self.get_object().author == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Blog'
        context['form_title'] = 'Update Blog'
        context['form_btn'] = 'Update'
        context['with_media'] = True
        return context


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = BlogModel
    template_name = 'core/blog_delete.html'
    success_url = reverse_lazy('home')  # Redirect to the home page after deletion
    context_object_name = 'blog'
    success_message = 'The blog post was successfully deleted.'
    
    def test_func(self):
        # Check if the authenticated user is the author of the blog
        return self.get_object().author == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Blog'
        return context
    
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogModel

@login_required
def blog_list(request):
    # Lấy danh sách bài viết của user hiện tại theo thứ tự mới nhất
    posts = BlogModel.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'core/blog_list.html', {'posts': posts})


@login_required
def delete_blog_posts(request):
    # Chỉ chấp nhận yêu cầu POST
    if request.method != 'POST':
        messages.error(request, "Yêu cầu không hợp lệ!")
        return redirect('blog_list')
    
    # Lấy danh sách id bài viết được chọn từ form
    post_ids = request.POST.getlist('post_ids')
    if not post_ids:
        messages.warning(request, "Không có bài viết nào được chọn!")
        return redirect('blog_list')
    
    # Lọc các bài viết thuộc về user hiện tại có id trong danh sách
    posts = BlogModel.objects.filter(id__in=post_ids, author=request.user)
    count = posts.count()
    
    if count:
        posts.delete()
        messages.success(request, f"Đã xóa {count} bài viết thành công!")
    else:
        messages.warning(request, "Không tìm thấy bài viết nào cần xóa hoặc bạn không có quyền xóa.")
    
    return redirect('blog_list')

