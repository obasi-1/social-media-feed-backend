from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from users.views import PostListCreateView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from users.views import RegisterView, ProfileView, LikePostView, profile_view
from django.shortcuts import redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("users.urls")),  # All API endpoints will start with /api/
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/profile/", ProfileView.as_view(), name="profile"),
    path("api/posts/", PostListCreateView.as_view(), name="posts"),
    path("api/posts/<int:post_id>/like/", LikePostView.as_view(), name="like-post"),
    path("api/profile/", profile_view, name="profile"),
        path("", lambda request: redirect("/api/")),

]
