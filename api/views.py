from django.shortcuts import get_object_or_404
from users.models import User
from .serializers import UserSerializers
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView



class UserViewsApi(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers



class GetUserViewsApi(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
    def get_object(self):
        return get_object_or_404(User, user_id=self.kwargs.get('pk'))

