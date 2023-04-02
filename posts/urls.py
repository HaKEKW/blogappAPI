from django.urls import path

from posts.views import PostList, PostDetail


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail_url'),
    path('', PostList.as_view(), name='post_list_url'),
]