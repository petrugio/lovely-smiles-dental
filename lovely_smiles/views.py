from datetime import timedelta, date
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
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
        form.fields['appointment_time'].widget = TimePickerInput(attrs={
            "placeholder": "Mon-Fri: 8am-5pm, Sat: 8am-1pm"})
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


class ListAppointmentsView(LoginRequiredMixin, ListView):
    """
    View to render view appointments
    and allow user to manage a appointments
    """
    template_name = 'lovely_smiles/view_appointments.html'
    model = Appointment

    def get_queryset(self):
        """ Queryset function to display appointments """

        if self.request.user.is_staff:
            # returns all appointments within last 5 days
            return Appointment.objects.filter(
                appointment_date__gt=(date.today()-timedelta(days=5))
                )
        else:
            # returns all appointments for logged in patient
            # with date greater than yesterday
            return Appointment.objects.filter(
                user=self.request.user,
                appointment_date__gt=(date.today()-timedelta(days=1))
                )


class EditAppointmentsView(LoginRequiredMixin,
                           UserPassesTestMixin, UpdateView):
    """
    A view to provide a form to the user
    to edit an appointment
    """
    form_class = MakeAppointmentForm
    template_name = 'lovely_smiles/edit_appointments.html'
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
        Check if the form is valid
        """
        patient_name = form.cleaned_data['patient_name']
        date = form.cleaned_data['appointment_date']
        time = form.cleaned_data['appointment_time']

        messages.success(
            self.request,
            f'Successfully updated appointment , \
                for {patient_name} on {date} at {time}'
        )
        return super(EditAppointmentsView, self).form_valid(form)

    def test_func(self):
        """ Test if the user is the owner or is staff else show 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user


class DeleteAppointmentView(SuccessMessageMixin, LoginRequiredMixin,
                            UserPassesTestMixin, DeleteView):
    """ A view to delete a appointment """
    model = Appointment
    success_url = "/appointments"
    success_message = "Appointment deleted!"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteAppointmentView, self).delete(
            request, *args, **kwargs)

    def test_func(self):
        """ Test if the user is the owner or is staff else show 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user
