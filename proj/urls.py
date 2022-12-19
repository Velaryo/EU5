"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from todos.views import index


urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/users/", include('users.urls'), name='users'),
	path(r"api/v1/", include('myApp.urls'), name='myApp'),
	path(r"api/v2/", include('pagos_v2.urls'), name='pagos_v2')
]

# http://127.0.0.1:8000/api/users/
# http://127.0.0.1:8000/api/users/login/
# http://127.0.0.1:8000/api/users/signup/

# http://127.0.0.1:8000/api/v1/pagos/

# http://127.0.0.1:8000/api/v2/services/
# http://127.0.0.1:8000/api/v2/payments/