from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views

router = routers.DefaultRouter()

router.register('', views.GetUsers)

urlpatterns = [
    path(r"signup/", views.SignUpView.as_view(), name="signup"),
    path(r"login/", views.LoginView.as_view(), name= "login"),
    path(r"jwt/create/", TokenObtainPairView.as_view(), name= "jwt_create"),
    path(r"jwt/refresh/", TokenRefreshView.as_view(), name= "token_refresh"),
    path(r"jwt/verify/", TokenVerifyView.as_view(), name= "token_verify"),

]

urlpatterns += router.urls