from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()

@staff_member_required
def user_management(request):
    """
    Trang admin quản lý người dùng: admin có thể khóa/mở khóa user và reset mật khẩu.
    """
    users = User.objects.all()
    if request.method == "POST":
        action = request.POST.get("action")
        user_id = request.POST.get("user_id")
        user = get_object_or_404(User, pk=user_id)
        
        if action == "block":
            user.is_blocked = True
            user.save()
            messages.success(request, f"Người dùng {user.username} đã bị khóa.")
        elif action == "unblock":
            user.is_blocked = False
            user.save()
            messages.success(request, f"Người dùng {user.username} đã được mở khóa.")
        elif action == "reset_password":
            # Reset mật khẩu về một giá trị mặc định (hoặc có thể tạo random)
            new_password = "default123"
            user.set_password(new_password)
            user.save()
            messages.success(request, f"Mật khẩu của {user.username} đã được reset thành: {new_password}")
        return redirect("user_management")
    
    context = {"users": users}
    return render(request, "core/admin_users.html", context)
