from rest_framework import routers
from django.urls import include, path
from api.views import PostViewSet, GroupViewSet
from api.views import CommentViewSet, UserViewSet, FollowViewSet


v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'users', UserViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
v1_router.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
