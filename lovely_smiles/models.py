from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Services choices
SERVICES = (
    ("Consultation", "Consultation"),
    ("Bridges", "Bridges"),
    ("Crowns", "Crowns"),
    ("Fillings", "Fillings"),
    ("Canal", "Root canal treatment"),
    ("Scale", "Scale and polish"),
    ("Braces", "Braces"),
    ("Wisdom", "Wisdom tooth removal"),
    ("Implants", "Dental implants"),
    ("Dentures", "Dentures or false teeth"),
    ("Whitening", "Teeth whitening"),
    ("Veneers", "Dental veneers")
)

# Dentists choices
DENTISTS = (
    ("Dr_Becket", "Dr. Becket"),
    ("Dr_Giku", "Dr. Giku")
)


class Appointment(models.Model):
    """ Model to create an appointment """
    patient_name = models.CharField(max_length=45)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointment_user")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    dentist = models.CharField(
        max_length=25, choices=DENTISTS, default="first_dentist")
    service = models.CharField(
        max_length=25, choices=SERVICES, default="consultation")
    phone = PhoneNumberField(null=False, blank=False)

    class Meta:
        """ Order by appointment_date and then by appointment_time"""
        ordering = ['appointment_date', 'appointment_time']

    def __str__(self):
        return str(self.pk)
