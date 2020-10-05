from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mindmap import views as views_mm
from user import views as views_user
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


router = DefaultRouter()
router.register('mindmaps', views_mm.MindmapsViewSet)
router.register('users', views_user.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]