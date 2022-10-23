from datetime import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
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
        phone = PhoneNumberField()
        labels = {
            'patient_name': 'Patient name',
            'phone': 'Phone number',
            'dentist': 'Dentist',
            'service': 'Service',
            'appointment_date': 'Date',
            'appointment_time': 'Time',
        }

        appointment_date = forms.DateField(
            widget=DatePickerInput(format='%Y/%m/%d')
        )
        appointment_time = forms.TimeField(
            widget=TimePickerInput()
        )

