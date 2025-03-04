from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import BlogModel, CommentModel, LikeModel

CustomUser = get_user_model()

def block_users(modeladmin, request, queryset):
    queryset.update(is_blocked=True)
    block_users.short_description = "Khóa người dùng đã chọn"

def unblock_users(modeladmin, request, queryset):
    queryset.update(is_blocked=False)
    unblock_users.short_description = "Mở khóa người dùng đã chọn"

def reset_password(modeladmin, request, queryset):
    default_password = "123@123"  # Bạn có thể thay đổi mật khẩu mặc định tại đây
    for user in queryset:
        user.set_password(default_password)
        user.save()
    reset_password.short_description = "Reset mật khẩu cho người dùng đã chọn"

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_blocked', 'is_staff', 'is_superuser')
    actions = [block_users, unblock_users, reset_password]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_blocked', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)


from .models import BlogModel, CommentModel, LikeModel, SiteConfiguration


admin.site.register(SiteConfiguration)
