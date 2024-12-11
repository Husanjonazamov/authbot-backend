from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User


def home(request):
    user_id = request.GET.get('user_id')  # URL orqali user_id olish

    if not user_id:
        return render(request, 'home.html')  # Agar user_id bo'lmasa, home sahifasini ko'rsatish

    try:
        user = User.objects.get(user_id=user_id)

        if user.is_verified:
            return render(request, 'home.html')  
        else:
            return redirect(f'/verify?user_id={user_id}')  

    except User.DoesNotExist:
        return redirect('register')



def register(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'home.html')


def verify(request):
    user_id = request.GET.get('user_id')
    code = request.GET.get('code')
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "Foydalanuvchi topilmadi!"}, status=404)

    if request.method == "POST":
        entered_code = request.POST.get('code') 

        if entered_code == str(user.random_code):  
            user.is_verified = True
            user.save()
            return redirect('home')  

        else:
            return render(request, 'code.html', {
                'user_id': user_id,
                'code': code,
                'error': 'Tasdiqlash kodi noto‘g‘ri!'
            })

    return render(request, 'code.html', {'user_id': user_id, 'code': code})


