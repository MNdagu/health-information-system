from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.

class HealthProgram(models.Model):
    """Model representing a health program (e.g., TB, Malaria, HIV, etc.)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    """Model representing a client in the health system"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    programs = models.ManyToManyField(HealthProgram, through='Enrollment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = timezone.now().date()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

class Enrollment(models.Model):
    """Model representing the enrollment of a client in a health program"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('client', 'program')

    def __str__(self):
        return f"{self.client} - {self.program}"
