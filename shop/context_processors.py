from .models import Category

def menu_links(request):
	links = Category.objects.all()#Все объекты модели категории
	return dict(links=links)#возвращает словаль с сылкамии
