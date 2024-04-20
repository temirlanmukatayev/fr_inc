from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import ClientCreationForm, WorkerCreationForm
from .models import Worker


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
