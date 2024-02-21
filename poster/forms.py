from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['placeholder'] = visible.field.label

	username = forms.CharField(max_length=256, label='Логин', widget=forms.TextInput)
	password = forms.CharField(max_length=256, label='Пароль', widget=forms.PasswordInput)


class RegForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['placeholder'] = visible.field.label

	username = forms.CharField(max_length=256, label='Логин')
	password = forms.CharField(max_length=256, label='<PASSWORD>')
	email = forms.CharField(max_length=256, label='E-mail')
