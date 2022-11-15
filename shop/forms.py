from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#UserCreationForm класс - используется, если хотим Usera по умолчанию
#В нём есть USERNAME and Password
#для добавления других полей мы и создаём класс
class SignUpForm(UserCreationForm):
	#required=True - поле не может быть пустым или иметь none
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	email = forms.EmailField(max_length=250, help_text='eg. youremail@yandex.ru')


	class Meta:# при создани -пользователь будет сохранятся в таблице User
		model = User
		#fields - поля
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')





