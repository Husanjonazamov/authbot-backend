# from django.shortcuts import render, redirect
# from .models import User


# class CheckUserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             try:
#                 user = User.objects.get(user_id=request.user.id)
#                 if not user.is_verified:
#                     return redirect('verify')
#             except User.DoesNotExist:
#                 return redirect('home')  

#         response = self.get_response(request)
#         return response
