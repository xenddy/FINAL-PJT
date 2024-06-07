from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # # 게시글 등록,수정,삭제
    path('Travel/', views.TravelList.as_view(), name='Travel_list'),
    path('Travel/<int:pk>/', views.TravelDetail.as_view(), name='Travel_detail'),
    path('newlist/', views.TravelList.get_new_post_page, name='newlist'),
    path('Camping/', views.CampingList.as_view(), name='Camping_list'),
    path('Camping/<int:pk>/', views.CampingDetail.as_view(), name='Camping_detail'),
    path('Leisure/', views.LeisureList.as_view(), name='Leisure_list'),
    path('Leisure/<int:pk>/', views.LeisureDetail.as_view(), name='Leisure_detail'),
    path('Cooking/', views.CookingList.as_view(), name='Cooking_list'),
    path('Cooking/<int:pk>/', views.CookingDetail.as_view(), name='Cooking_detail'),
    path('<int:article_id>/comments/', views.CommentGetPost.as_view(), name='comments-list'),
    path('comments/<int:comment_pk>/', views.CommentPutDelete.as_view(), name='comments-create'),
    # #좋아요
    path('like/<int:article_id>/', views.LikeCreate.as_view(), name='like-create'),

]