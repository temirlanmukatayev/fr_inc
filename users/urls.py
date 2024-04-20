from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/client/', views.SignUpClientView.as_view(), name='signup_client'),
    path('signup/worker/', views.SignUpWorkerView.as_view(), name='signup_worker'),
]