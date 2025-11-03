from rest_framework import generics
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# API endpoint để lấy thông tin health check
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'message': 'django_api API is running!'
    })
