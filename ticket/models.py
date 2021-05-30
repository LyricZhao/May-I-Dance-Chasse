from django import forms
from django.db import models

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

from chasse.settings import BASE_DIR

TICKET_SOURCE_FILE = BASE_DIR / 'static' / 'images' / 'ticket.png'
TICKET_SAVE_PATH = BASE_DIR / 'static' / 'tickets'

class TicketForm(forms.Form):
    name = forms.CharField(max_length=32)
    pid = forms.CharField(max_length=32)

class Ticket(models.Model):
    name = models.CharField(max_length=32)
    pid = models.CharField(max_length=32)
    hash_value = models.CharField(max_length=32, unique=True)

    def make(self):
        print(str(TICKET_SOURCE_FILE))
        with Image(filename=str(TICKET_SOURCE_FILE)) as ticket:
            with Drawing() as draw:
                draw.push()
                draw(ticket)
                ticket.save(filename=str(TICKET_SAVE_PATH / (self.hash_value + '.png')))
