"""ecommerce URL Configuration

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
from django.urls import path, include #импортировали всё
from django.conf import settings #импортировали
from django.conf.urls.static import static #импортировали


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),#На пустой запрос Localhost, будет ссылаться в shop/urls.py
]

#Для обновление url-ов в Дебаг моде
if settings.DEBUG:#if settings.DEBUG = True
    #в список путей будут добавлятся пути MEDIA_URL и MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

#аналогично для статик папки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

