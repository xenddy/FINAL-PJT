
from django.urls import path
from . import views
from .views import FollowToggleViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path("", views.UserSignupView.as_view(), name="users"), 
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("<str:username>/",views.UserDetailAPIView.as_view(),name="user-detail"),
    path('follow/<str:username>/', FollowToggleViewSet.as_view({'post': 'create'})),
]

