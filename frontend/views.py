from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from rest_framework.views import APIView
import logging
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer

logger = logging.getLogger(__name__)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                refresh = RefreshToken.for_user(user)
                response = JsonResponse({'detail': '로그인 성공', 'refresh': str(refresh), 'access': str(refresh.access_token)})
                response.set_cookie('access_token', str(refresh.access_token), httponly=True)
                response.set_cookie('refresh_token', str(refresh), httponly=True)
                next_url = request.POST.get('next', 'articles:Camping_list')
                response['Location'] = next_url
                return response
            else:
                logger.debug(f'User {username} authentication failed')
                return render(request, 'frontend/login.html', {'form': form, 'error': 'Invalid login details'})
        else:
            logger.debug('Form is not valid')
            return render(request, 'frontend/login.html', {'form': form, 'error': 'Invalid form details'})
    else:
        form = AuthenticationForm()
    return render(request, 'frontend/login.html', {'form': form})

def signup(request):
    return render(request, 'frontend/signup.html')

def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'frontend/user_detail.html', {'user': user})

def logout(request):
    auth_logout(request)
    return redirect('articles:Camping_list')

class UserEditView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, 'frontend/useredit.html', {'user': user})

def index(request):
    return render(request, 'frontend/index.html')