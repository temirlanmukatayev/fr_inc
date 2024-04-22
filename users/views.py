from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import client_required, worker_required

from .forms import ClientCreationForm, WorkerCreationForm
from .models import Worker
from orders.models import Order


User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class SignUpClientView(CreateView):
    template_name = 'registration/signup_client.html'
    model = User
    form_class = ClientCreationForm
    success_url = reverse_lazy('login')


class SignUpWorkerView(CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'registration/signup_worker.html'
    success_url = reverse_lazy('login')


@method_decorator([login_required, client_required], name='dispatch')
class ClientCabinetView(TemplateView):
    template_name = 'client_cabinet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['orders'] = Order.objects.filter(author=self.request.user)
        return context


@method_decorator([login_required, worker_required], name='dispatch')
class WorkerCabinetView(TemplateView):
    template_name = 'worker_cabinet.html'
