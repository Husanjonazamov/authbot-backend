from django.urls import path
from .views import home, login, verify, register



urlpatterns = [
    path('verify/', verify, name='verify'),
    path('home/', home, name='home'),
    path('', register, name='register'),
    path('login/', login, name='login'),
    
]

