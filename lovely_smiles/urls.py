
from django.urls import path
from . import views

urlpatterns = [
    path(
        'make_appointment/', views.CreateAppointmentView.as_view(),
        name='make_appointment'
        ),
    path(
        'appointments/', views.ListAppointmentsView.as_view(),
        name='appointments'
        ),
    path(
        'edit_appointment/<slug:pk>', views.EditAppointmentsView.as_view(),
        name='edit_appointment'
        ),
    path(
        'delete_appointment/<slug:pk>', views.DeleteAppointmentView.as_view(),
        name='delete_appointment'
        ),
    path(
        '', views.HomeView.as_view(),
        name='home'
       ),
    path(
        'services', views.ServicesView.as_view(),
        name='services'
       )
]
