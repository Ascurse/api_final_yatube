from django.urls import path, include
from rest_framework.authtoken import views
from api.views import CommentViewSet, PostViewSet, GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts/(?P<id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls))
]
