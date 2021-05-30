from django import forms
from django.db import models

class TicketForm(forms.Form):
    name = forms.CharField(max_length=32, label='姓名')
    stu_id = forms.IntegerField(max_value=9999999999, min_value=1000000000, label="学号")

class Ticket(models.Model):
    stu_id = models.IntegerField(blank=True, default=0)
