from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from users.decorators import client_required, worker_required
from .models import Order, OrderStatus, WorkerOrder
from .mixins import AuthorOnlyMixin


class OrderListView(ListView):
    '''Listing all client orders for public access.'''
    model = Order
    context_object_name = 'orders'
    template_name = 'order_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Order.objects.filter(status=OrderStatus.NEW)
        return queryset


@method_decorator([client_required,], name='dispatch')
class OrderCreateView(CreateView):
    '''Creating a new order by client.'''
    model = Order
    fields = ['title', 'description',]
    template_name = 'order_create.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

@method_decorator([client_required,], name='dispatch')
class OrderUpdateView(AuthorOnlyMixin, UpdateView):
    '''Updating order details by client (only author).'''
    model = Order
    fields = ['title', 'description', 'status',]
    template_name = 'order_update.html'
    success_url = reverse_lazy('client_cabinet')
    

class OrderDetailView(DetailView):
    '''Order details for public access.'''
    model = Order
    context_object_name = 'order'
    template_name = 'order_detail.html'
