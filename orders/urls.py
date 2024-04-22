from django.urls import path

from .views import OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView

urlpatterns = [
    path('list/', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
]