from django.urls import path
from . import views
from articles.views import LatestPosts  # 올바른 앱에서 가져오기

app_name = 'frontend'

urlpatterns = [
    path("users/signup/", views.signup, name="signup"),
    path("users/login/", views.login, name="login"),
    path("users/logout/", views.logout, name="logout"),
    path('users/<str:username>/', views.user_detail, name="user_detail"),
    path('users/<str:username>/edit/', views.UserEditView.as_view(), name='user-edit'),
    path('latest/<str:category>/', LatestPosts.as_view(), name='latest_posts'),  # 올바른 경로로 변경
    path('', views.index, name='index'),
]
