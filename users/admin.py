from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'random_code',)
    
    
    
admin.site.register(User, UserAdmin)
