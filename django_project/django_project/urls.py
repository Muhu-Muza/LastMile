"""django_project URL Configuration

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
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from account import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', user_views.index, name='home'),
    path('base/', user_views.base, name='base'),
    path('services/', user_views.services, name='services'),
    path('about/', user_views.about, name='about'),
    path('contact/', user_views.contact, name='contact'),
    path('sender_dashboard/', user_views.sender_dashboard, name='sender_dashboard'),
    path('register_package/', user_views.register_package, name='register_package'),
]
