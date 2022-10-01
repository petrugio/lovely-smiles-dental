
from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.HomeView.as_view(),
        name='home'
       ),
    path(
        'services', views.ServicesView.as_view(),
        name='services'
       ),
    path(
        'makeappointment/', views.CreateAppointmentView.as_view(),
        name='makeappointment'
        )
]
