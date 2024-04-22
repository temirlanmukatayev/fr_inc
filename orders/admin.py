from django.contrib import admin

from .models import Order, WorkerOrder


admin.site.register(Order)
admin.site.register(WorkerOrder)
