from django.urls import path#скопировали из основного urls.py
from . import views#импортировали shop/views.py




urlpatterns = [
    path('', views.home, name='home'),#пустой url к функции home в shop/views.py, присвоили имя home
    path('product/', views.product, name='product'),
]
