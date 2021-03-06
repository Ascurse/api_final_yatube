from django.urls import path, include
from api.views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts/(?P<id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
