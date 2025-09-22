from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from users.views import PostListCreateView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from users.views import RegisterView, ProfileView, LikePostView, profile_view
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version="v1",
        description="API documentation for the Social Media project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="youremail@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", lambda request: redirect("/api/")),

]