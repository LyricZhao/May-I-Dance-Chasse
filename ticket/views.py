from django.shortcuts import render

from .models import Ticket, TicketForm

MAX_TICKETS = 1000

def index(request):
    count = Ticket.objects.all().count()
    ticket_left = MAX_TICKETS - count
    if ticket_left <= 0:
        ticket_ready = False
        return render(request, 'index.html', locals())
    else:
        ticket_ready = True
        return render(request, 'index.html', locals())


def ticket(request):
    return render(request, 'ticket.html')
