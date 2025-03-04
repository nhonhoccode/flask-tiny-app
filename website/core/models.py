from django.urls import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_blocked = models.BooleanField(default=False, verbose_name="Đã khóa")
    is_admin = models.BooleanField(default=False, verbose_name="Quản trị viên")

class BlogModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    media = models.ImageField(upload_to='blog_media/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"

class LikeModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.blog.title}"


class SiteConfiguration(models.Model):
    paginate_by = models.PositiveIntegerField(
        default=10, 
        help_text="Số bài viết được hiển thị trên mỗi trang."
    )

    def __str__(self):
        return f"Cấu hình (paginate_by = {self.paginate_by})"

