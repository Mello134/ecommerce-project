from django.shortcuts import render
# from django.http import HttpResponse #импоприровали htth response
#HttpResponse больше не нужен - будем пользоваться render-ом

# Create your views here.
def home(request):
	return render(request, 'home.html')#путь к ecommerce/shop/templates/home.html

def about(request):
	return render(request, 'about.html')
