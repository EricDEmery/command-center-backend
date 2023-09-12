from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from commandcenter.views import *
from commandcenter import views


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', views.UserSearch),
    path('posts/', PostViewSet.as_view)
]