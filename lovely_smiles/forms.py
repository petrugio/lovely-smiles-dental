import datetime
from django.core.exceptions import ValidationError
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
            widget=DatePickerInput()
        )
        appointment_time = forms.TimeField(
            widget=TimePickerInput()
        )

    def clean(self):
        """
        Check if appointment within working hours or
        not in the past and show errors when appointment cannot be made
        """
        date = self.cleaned_data['appointment_date']
        time = self.cleaned_data['appointment_time']

        selected_date_with_time = datetime.datetime.combine(date, time)

        if selected_date_with_time < datetime.datetime.now():
            raise ValidationError(
                'Invalid date or time - Appointment cannot be in the past')

        working_hours = [
            [datetime.time(hour=8), datetime.time(hour=16, minute=59)],
            [datetime.time(hour=8), datetime.time(hour=16, minute=59)],
            [datetime.time(hour=8), datetime.time(hour=16, minute=59)],
            [datetime.time(hour=8), datetime.time(hour=16, minute=59)],
            [datetime.time(hour=8), datetime.time(hour=16, minute=59)],
            [datetime.time(hour=8), datetime.time(hour=12, minute=59)],
            [datetime.time(hour=1), datetime.time(hour=0, minute=59)],
        ]

        selected_day = working_hours[selected_date_with_time.weekday()]
        if selected_date_with_time.time() < selected_day[0]\
                or selected_date_with_time.time() > selected_day[1]:
            raise ValidationError('Invalid time -\
                Hours for appointments are : Mon-Fri: 8am-5pm, Sat: 8am-1pm')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient_name'].widget.attrs.update({
            'placeholder': 'Ex: John'})
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Ex: +353868401577'})
