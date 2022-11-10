from django.db import models

# Create your models here.


#cсоздали класс категории
#унаследовали этому классу все фичи models.Model
class Category(models.Model):
	
	#models.CharField поле для строк малого и большого размера
	#max_length=250 - длина максимум 250
	#unique=True - поле будет уникальным и оно будет присваивать инжекс
	name = models.CharField(max_length=250, unique=True)
	
	#Slug - газетный термин. Слаг - это короткая метка для чего-либо, содержащая только буквы, цифры, подчеркивания или дефисы. Они обычно используются в URL.
	slug = models.SlugField(max_length=250, unique=True)
	
	#models.TextField - Большое текстовое поле. Виджет формы по умолчанию для этого поля Textarea.
	#blank=True - если вы хотите разрешить пустые значения в формах, как для строковых, так и для нестроковых полей
	description = models.TextField(blank = True)
	
	#ImageField - изображение. Наследует все атрибуты и методы из FileField, но также проверяет, что загруженный объект является допустимым изображением.
	#upload_to='category' - путь, будет загружать в папку category
	#null=True - Это свойство позволяет базе данных оставлять поле пустым, если мы добавили пост в базу данных, но ещё не опубликовали.
	#blank=True - Если null=True управляет поведением базы данных, тоblank=True настраивает поведение админки и Django-форм.
	#Если для поля published_at не указан blank=True, то админка запретит нам сохранить пост, и потребует заполнить поле published_at.
	image = models.ImageField(upload_to='category', blank=True)

	# Отображение в админке класса
	class Meta:
		ordering = ('name',)
		verbose_name = "Категория" #имя в единственном числе
		verbose_name_plural = "Категории" #имя во множественном числе





	#для того чтобы когда мы каждый раз будем обращатся к объекту категории, будет показыватся имя - название поля
	#Метод __str__() - вызывается всякий раз, когда вы вызываете str() для объекта.
	#self - собственный- личный
	def __str__(self):

		#Будет показывать имя модели (name переменная, указали выше)
		return self.name



#модель Товаров/продуктов
class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank = True)

	#Отношения многие-к-одному. Требуются два позиционных аргумента: класс, к которому относится модель, и опция
	#те каждый продукт может быть соединён с одной категорией, а одна категория может относится к несольким продуктам
	#Сategoty - Обращаемся к модели/классу категории
	#on_delete= - При удалении объекта, на который ссылается ForeignKey, Django будет эмулировать поведение ограничения SQL, заданного аргументом on_delete
	#Каскадное удаление. Django эмулирует поведение ограничения SQL ON DELETE CASCADE, а также удаляет объект, содержащий ForeignKey
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	#Десятичное число с фиксированной точностью, представленное в Python экземпляром
	#max_digits - Максимально допустимое количество цифр в номере. Обратите внимание, что это число должно быть больше или равн
	#decimal_places - Количество десятичных разрядов для хранения с числом.
	price = models.DecimalField(max_digits=10, decimal_places=2)

	image = models.ImageField(upload_to='product', blank=True)

	#Целое число. Значения от -2147483648 до 2147483647 безопасны
	stock = models.IntegerField()

	#BooleanField - Поле истина/ложь.
	#default=True - стандартно есть в наличии
	available = models.BooleanField(default=True)

	#Поле дата время
	#auto_now_add - Автоматически установить поле на сейчас, когда объект создается впервы
	created = models.DateTimeField(auto_now_add=True)

	#auto_now - Автоматически устанавливать текущую дату каждый раз, когда объект сохраняется.
	updated = models.DateTimeField(auto_now=True)

	
	# Отображение в админке класса
	class Meta:
		ordering = ('name',)
		verbose_name = "Продукт" #имя в единственном числе
		verbose_name_plural = "Продукты" #имя во множественном числе


	def __str__(self):
		return self.name




