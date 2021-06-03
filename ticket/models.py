from django import forms
from django.db import models

from PIL import Image, ImageDraw, ImageFont

from chasse.settings import BASE_DIR

TICKET_SOURCE_FILE = BASE_DIR / 'static' / 'images' / 'ticket.png'
TICKET_SAVE_PATH = BASE_DIR / 'static' / 'tickets'
FONT_PATH = BASE_DIR / 'static' / 'fonts' / 'FZXinZYHJW_R.ttf'

font = ImageFont.truetype(str(FONT_PATH), 26)

class TicketForm(forms.Form):
    name = forms.CharField(max_length=6)
    pid = forms.CharField(max_length=18)

class Ticket(models.Model):
    name = models.CharField(max_length=32)
    pid = models.CharField(max_length=32)
    hash_value = models.CharField(max_length=32, unique=True)

    def make(self):
        line = str(self.name) + ' / ' + str(self.pid)
        ticket = Image.open(str(TICKET_SOURCE_FILE))
        w, h = ticket.size
        draw = ImageDraw.Draw(ticket)
        lw, lh = draw.textsize(line, font=font)
        draw.text((520, 129), line, fill='white', font=font)
        ticket.save(str(TICKET_SAVE_PATH / (self.hash_value + '.png')), 'PNG')
