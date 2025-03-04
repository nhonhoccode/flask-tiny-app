from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from core.models import BlogModel

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with sample blog posts for pagination simulation.'

    def handle(self, *args, **kwargs):
        # Lấy hoặc tạo user test để làm tác giả cho các bài viết mẫu
        user, created = User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'})
        if created:
            user.set_password('password123')
            user.save()

        # Tạo 100 bài viết mẫu
        for i in range(1, 101):
            BlogModel.objects.create(
                title=f'Post {i}',
                content=f'This is the content for post {i}.',
                author=user,
                created_at=timezone.now()
            )
            self.stdout.write(self.style.SUCCESS(f'Created Post {i}'))

        self.stdout.write(self.style.SUCCESS('Database populated with sample posts.'))
