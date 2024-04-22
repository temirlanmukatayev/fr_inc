from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class OrderStatus(models.TextChoices):
        NEW = 'N', 'Новый'
        PENDING = 'P', 'На рассмотрении'
        APPROVED = 'A', 'Согласован'
        WORKING = 'W', 'В работе'
        FINISHED = 'F', 'Выполнен'


class Order(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=1, choices=OrderStatus,
                              default=OrderStatus.NEW, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self) -> str:
        return f'Заказ {self.pk}'


class WorkerOrder(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=OrderStatus,
                              default=OrderStatus.NEW, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return f'Запрос {self.pk}'
