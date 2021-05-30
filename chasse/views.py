from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ticket(request):
    return render(request, 'ticket.html')