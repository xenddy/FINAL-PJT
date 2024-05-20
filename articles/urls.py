from django.urls import path
from . import views


urlpatterns = [
    # 게시글 등록,수정,삭제
    path('', views.ArticleList.as_view(), name='Articles_list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='Articles_detail'),
]