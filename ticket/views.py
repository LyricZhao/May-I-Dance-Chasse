# -*- coding: utf-8 -*-

import sys
import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Ticket, TicketForm

MAX_TICKETS = 1000

logger = logging.getLogger('django')

def ticket_hash(name, pid):
    hash_value = hash(name + '/ticket/' + pid)
    hash_value += sys.maxsize + 1
    return str(hash_value)

def index(request):
    title = u'追·Chassé | 在线订票'
    error = []
    count = Ticket.objects.all().count()
    ticket_left = MAX_TICKETS - count
    if ticket_left <= 0:
        ticket_ready = False
        return render(request, 'index.html', locals())
    else:
        ticket_ready = True
        if request.method == 'GET':
            form = TicketForm()
        else:
            form = TicketForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                hash_value = ticket_hash(data['name'], data['pid'])
                ticket_filter = Ticket.objects.filter(hash_value=hash_value)
                if not ticket_filter.count():
                    logger.info('Generating ticket for ({}, {})'.format(data['name'], data['pid']))
                    ticket = Ticket(name=data['name'], pid=data['pid'], hash_value=hash_value)
                    ticket.save()
                    ticket.make()
                return HttpResponseRedirect('/ticket/' + hash_value + '/')
            else:
                error.append('请正确填写对应的信息！')
        return render(request, 'index.html', locals())


def ticket(request, hash_value):
    title = u'追·Chassé | 电子门票'
    ticket = Ticket.objects.get(hash_value=hash_value)
    return render(request, 'ticket.html', locals())
