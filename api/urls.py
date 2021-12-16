from django.urls import path, include
from .views import *

app_name = 'api'
urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('api/', PostList.as_view(), name='api-list'),
    path('api/<int:pk>', PostDetail.as_view(), name='api-detail'),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('like/', LikeList.as_view()),
    path('like/<int:pk>/', LikeDetail.as_view()),
]
