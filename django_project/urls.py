from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("posts/", include("posts.urls")),
    path("api/v1/", include("API1.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"),name="redoc",), 
    path("api/schema/swagger-ui/",SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    path("", include("pages.urls")),
]
