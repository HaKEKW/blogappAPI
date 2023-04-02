from django.urls import path
from rest_framework.routers import SimpleRouter

from posts.views import PostList, PostDetail, UserList, UserViewSet, PostViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename='users')
router.register('', PostViewSet, basename='users')

urlpatterns = [
    path('users/', UserList.as_view(), name='user_list_url'),
    path('users/<int:pk>/', UserList.as_view(), name='user_list_url'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail_url'),
    path('', PostList.as_view(), name='post_list_url'),
]

urlpatterns += router.urls