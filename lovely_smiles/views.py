from datetime import timedelta, date
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Appointment
from .forms import MakeAppointmentForm


class ServicesView(TemplateView):
    """
    View to render services page
    """
    template_name = 'lovely_smiles/services.html'


class HomeView(TemplateView):
    """
    View to render services page
    """
    template_name = 'lovely_smiles/index.html'


class CreateAppointmentView(LoginRequiredMixin, CreateView):
    """
    View to create an appointment
    """
    form_class = MakeAppointmentForm
    template_name = 'lovely_smiles/make_appointment.html'
    success_url = "/appointments/"
    model = Appointment

    def get_form(self):
        """
        Form date and time input
        """
        form = super().get_form()
        form.fields['appointment_date'].widget = DatePickerInput()
        form.fields['appointment_time'].widget = TimePickerInput()
        return form

    def form_valid(self, form):
        """
        Form validation
        """
        patient_name = form.cleaned_data['patient_name']
        form.instance.user = self.request.user
        date = form.cleaned_data['appointment_date']
        time = form.cleaned_data['appointment_time']

        messages.success(
            self.request,
            f'Appointment confirmed for {patient_name} on {date} at {time}'
        )

        return super(CreateAppointmentView, self).form_valid(form)
