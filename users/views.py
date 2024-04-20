from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
