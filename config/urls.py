"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import config.views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("facility/", include("facility.urls")),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("main/", views.main_page, name="main"),
    path("index/", views.index_page, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
