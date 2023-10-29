from django.shortcuts import render
from .models import Event
from authentication.models import Student
# Create your views here.


def home_view(request):

    student_bhawan = Student.objects.get(user=request.user).bhawan
    events = Event.objects.all().order_by('start_time').filter(bhawan_specifier='All') | Event.objects.all().order_by('start_time').filter(bhawan_specifier=student_bhawan)
    filter_toggles = {'Technical': 'on', 'Cultural': 'on',
                      'Bhawan-Related': 'on', 'Misc.': 'on'}
    
    date = ""

    if request.method == 'POST':
        all_events = Event.objects.all().order_by('start_time').filter(bhawan_specifier='All') | Event.objects.all().order_by('start_time').filter(bhawan_specifier=student_bhawan)

        for key in filter_toggles:
            filter_toggles[key] = request.POST.get(key)

        date = request.POST.get('date_input')
        events = []

        for event in all_events:
            if filter_toggles[event.event_type] == 'on':
                if (date != "" and str(event.start_time)[:10] >= str(date)) or date == "":
                    events.append(event)

    context = {'events': events,
               'filter_toggles': filter_toggles, 'date': date}
    return render(request, "home.html", context)
