from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

class BlockedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            # Nếu trường is_blocked có tồn tại và bằng True
            if getattr(request.user, 'is_blocked', False):
                messages.error(request, "Tài khoản của bạn đã bị khóa.")
                logout(request)
                return redirect('login')  # Chuyển hướng đến trang đăng nhập hoặc trang thông báo khác
                
        response = self.get_response(request)
        return response
