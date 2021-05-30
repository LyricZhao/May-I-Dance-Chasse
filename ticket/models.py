from django import forms
from django.db import models

class TicketForm(forms.Form):
    name = forms.CharField(max_length=32)
    pid = forms.CharField(max_length=32)

class Ticket(models.Model):
    name = models.CharField(max_length=32)
    pid = models.CharField(max_length=32)
    hash_value = models.CharField(max_length=32, unique=True)
