from django.urls import path#скопировали из основного urls.py
from . import views#импортировали shop/views.py




urlpatterns = [
    path('', views.home, name='home'),#пустой url к функции home в shop/views.py, присвоили имя home
    path('category/<slug:category_slug>', views.home, name='products_by_category'),#путь URL по нашему слагу localhost/../имя slug-a
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.signUpView, name='signup'),
]
