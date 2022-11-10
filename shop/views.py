from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse #импоприровали htth response
#HttpResponse больше не нужен - будем пользоваться render-ом
from .models import Category, Product



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

def product(request):
	return render(request, 'product.html')
