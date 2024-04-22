from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/client/', views.SignUpClientView.as_view(), name='signup_client'),
    path('signup/worker/', views.SignUpWorkerView.as_view(), name='signup_worker'),
    path('client/cabinet/', views.ClientCabinetView.as_view(), name='client_cabinet'),
    path('worker/cabinet/', views.WorkerCabinetView.as_view(), name='worker_cabinet'),
]