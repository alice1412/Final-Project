
from django.urls import path, include
from .views import PostsView, MindmapsViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

from rest_framework.routers import DefaultRouter
# from mindmap import views as views_mm
# from user import views as views_user

urlpatterns = [
    # path('api-token/', TokenObtainPairView.as_view()),
    # path('api-token-refresh/', TokenRefreshView.as_view()),
    path('posts/', PostsView.as_view()),
]

# router = DefaultRouter()
# router.register('mindmaps', MindmapsViewSet)
# # router.register('users', views_user.UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]