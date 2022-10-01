from datetime import datetime
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Appointment


class MakeAppointmentForm(forms.ModelForm):
    """
    Form to create and edit an appointment
    """
    class Meta:
        """ Set fields and labels """
        model = Appointment
        fields = [
            'patient_name',
            'phone',
            'dentist',
            'service',
            'appointment_date',
            'appointment_time',
            ]
        appointment_date = forms.DateField(
            help_text="Date must be a future date")
        appointment_time = forms.TimeField(
            help_text="Time must be in working hours interval")
        phone = PhoneNumberField()
        labels = {
            'patient_name': 'Patient name',
            'phone': 'Phone number',
            'dentist': 'Dentist',
            'service': 'Service',
            'appointment_date': 'Date',
            'appointment_time': 'Time',
        }

    def clean(self):
        """
        Get form data and clean, check capacity and
        throw errors when tables not available
        """
        date = self.cleaned_data['appointment_date']
        time = self.cleaned_data['appointment_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appointment_date'].widget.attrs['class'] = 'datepicker'
        self.fields['appointment_date'].widget.attrs['autocomplete'] = 'off'
