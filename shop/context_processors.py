from .models import Category, Cart, CartItem
from .views import _cart_id


def counter(request):
	item_count = 0
	#если в запросе есть admin
	if 'admin' in request.path:
		#возвратим пустой словарь, ничего делать не нужно
		return {}
	#иначе
	else:#иначе
		#если в корзине что то есть
		try:
			cart = Cart.objects.filter(cart_id=_cart_id(request))
			#[:1] - будет возвращатся только 1 обхект cart_item
			cart_items = CartItem.objects.all().filter(cart=cart[:1])
			for cart_item in cart_items:#проходим через каждый cart_item
				item_count += cart_item.quantity #прибавляем каждый quantity
		#если корзина пуста
		except Cart.DoesNotExist:
			item_count = 0
	#выводим словарь который содержит переменную item_count
	return dict(item_count=item_count)






def menu_links(request):
	links = Category.objects.all()#Все объекты модели категории
	return dict(links=links)#возвращает словаль с сылкамии
