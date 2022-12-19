from django.contrib import admin
from django.urls import path, include
from .views import index

from django.urls import re_path #para el RegexPattern
from drf_yasg.views import get_schema_view
#estandar que permite saber como documentar API
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
#generar schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Api de PAGOS",
        default_version="v2",
        description="API para el sistema de pagos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="abc@example.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[AllowAny]
)



urlpatterns = [
	path("", index, name='index'),
    path(r"admin/", admin.site.urls),
    path(r"api/users/", include('users.urls'), name='users'),
	path(r"api/v1/", include('myApp.urls'), name='myApp'),
	path(r"api/v2/", include('pagos_v2.urls'), name='pagos_v2'),

	re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json')

]
