from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Worker


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class ClientCreationForm(UserCreationForm):
    is_client = forms.BooleanField(
        label='Я клиент',
        help_text='Планирую размещать заказы для исполнителей'
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'is_client',)

    
class WorkerCreationForm(UserCreationForm):
    is_worker = forms.BooleanField(
        label='Я исполнитель',
        help_text='Планирую размещать выполнять заказы исполнителей'
    )
    experience = forms.IntegerField(
        label='Опыт работы',
        help_text='Укажите количество лет'
    )
    sphere = forms.CharField(
        label='Сфера',
        help_text='Укажите сферу деятельнсти'
    )
    description = forms.CharField(
        label='Описание',
        help_text='Этот текст будет виден в качестве описания вашего профиля'
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'is_worker', 'experience', 'sphere', 'description',)
