from django.urls import path
from . import views


urlpatterns = [

    path("users/signup/", views.signup, name="signup"),
    path("users/login/", views.login, name="login"),
    path('users/<str:username>/', views.user_detail, name="user_detail"),
    path('users/<str:username>/edit/', views.UserEditView.as_view(), name='user-edit'),
]