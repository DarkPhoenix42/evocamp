from django.shortcuts import render
from .models import Event
# Create your views here.


def home_view(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, "home.html", context)
