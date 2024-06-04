from django.shortcuts import render, get_object_or_404
from users.models import User
from rest_framework.views import APIView


def login(request):
    return render(request, 'frontend/login.html')

def signup(request):
    return render(request, 'frontend/signup.html')

def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'frontend/user_detail.html', {'user': user})

class UserEditView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, 'frontend/useredit.html', {'user': user})
    
