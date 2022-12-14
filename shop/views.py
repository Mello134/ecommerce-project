from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse #импоприровали htth response
#HttpResponse больше не нужен - будем пользоваться render-ом
from .models import Category, Product, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout



# Create your views here.
def home(request, category_slug=None):
	category_page = None
	products = None
	if category_slug != None:#если в category_slug что то есть
		category_page = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category_page, available=True)
	else:#если category_slug пустой
		products = Product.objects.all().filter(available=True)
	return render(request, 'home.html', {'category':category_page, 'products':products})#путь к ecommerce/shop/templates/home.html

def product(request, category_slug, product_slug):
	#category__slug - здесь получис slug из Сategory
	product = Product.objects.get(category__slug=category_slug, slug=product_slug)
	#exept - это исключения. Exception - класс исключений в python
	# raise - привликать, поднимать
	#код выполнится если будут исключения
	


	# except Exception as e: #SyntaxError: invalid syntax-------------------------------------------------
	# 	raise e #--------------------------------------------------------------------------------------------------------------------------------------
	

	return render(request, 'product.html', {'product': product})



#корзина будет сохраняемая в этой сессии пока пользователь будет на сайте
def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart


# add_cart - метод чтобы добавлять товары, обновлять их количчество в корзине, и комбинировать их в один cart_item Объект
def add_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	
	#преждевсего пытаемся получить объект cart - из текущей сессии
	try:
		#используем метод get - получить
		cart = Cart.objects.get(cart_id=_cart_id(request))

	#Если такого объекта нет, мы создаём пустой объект и присваиваем в переменной
	except Cart.DoesNotExist:#если корзины не существует
		#тогда создаём переменную cart и присваиваем Cart.objects Но уже используем метод create - создать новую корзину
		cart = Cart.objects.create(cart_id=_cart_id(request))
		#сохраняем состояние
		cart.save()

	#почти тоже самое для класса CartItem
	try:
		cart_item = CartItem.objects.get(product=product, cart=cart)
		
		if cart_item.quantity < cart_item.product.stock: #будем увеличивать только в этом случае
			cart_item.quantity += 1# обновляем количество

		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
		cart_item.save()

	#redirect - Переадрезация
	#перенаправляем пользователя на url cart_detail - чтобы обновить все элементы в корзине в текущей сессии
	return redirect('cart_detail') 


#функция будет извлекать все продукты и калькулировать полную сумму всех cart_item элементов в корзине
#изначатьно в итог сумма=0, количество элементов=0, в корзине нет элементов
def cart_detail(request, total=0, counter=0, cart_items=None):
	#пробуем получить в текущей сессии (если есть в корзине что то)
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart, active=True)
		#высчитываем total
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)#сумма
			counter += cart_item.quantity#количество

	#если получить в текущей сессии ничего не можем, тогда
	except ObjectDoesNotExist:
		pass#игнорируем

	return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id): #уменьшийть корзину
	cart = Cart.objects.get(cart_id=_cart_id(request))
	#находим продукт количество которого мы должны обновить используя get-404
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart_detail')


def cart_remove_product(request, product_id): #удалить полностью товар из корзины
	cart = Cart.objects.get(cart_id=_cart_id(request))
	#находим продукт количество которого мы должны обновить используя get-404
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	cart_item.delete()
	return redirect('cart_detail')


def signUpView(request):#для фсоздание аккаунта
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid(): #проверяем форму, valid-действительность
			form.save() #В этом случае сохраняем форму
			#мы будем находить пользователя из базы данных по username
			username = form.cleaned_data.get('username')
			signup_user  = User.objects.get(username=username)
			#помещаем usera - в группу которую мы создали в админке 'User'
			user_group = Group.objects.get(name='User')
			user_group.user_set.add(signup_user)#!!!??? возможно не сработает
	else: #если запрос не POST
		form = SignUpForm() #присваиваем пустую форму
	#будет выводится шаблон signup.html, и передовать переменную form в этот шаблон
	return render(request, 'signup.html', {'form':form})



def loginView(request): #для залогинивания
	if request.method == 'POST': #если метод POST
		form = AuthenticationForm(data=request.POST)#здесь есть data а в signUpView почемуто нет
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None: #если user сушествует
				login(request, user)
				return redirect('home')#направлемя домой path name='home'
			else: #если юзера не сушествует
				return redirect('signup')#направляем path('account/create/' - name='signup'
	else: #если метод не POST
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})


def signoutView(request): #Для выхода из аккаунта
	logout(request)#это втроенная функция django
	return redirect('login') #path('account/login/', views.loginView, name='login')




def contacts(request):#контакты
	return render(request,'contacts.html')

def about(request):#о нас
	return render(request,'about.html')







 