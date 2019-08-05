from django.shortcuts import render
from control.models import clarification, time

# Create your views here.

def index(request):

    lst = []
    for item in clarification.objects.all():
        lst.append(item.my_message[:])
    context = {'messages': lst}
    a = time.objects.all().first()
    context['start_time'] = a.start_time
    context['hours'] = a.hours
    context['minutes'] = a.minutes
    if a.start_time != 0:
        context['start_bool'] = True
    else:
        context['start_bool'] = False

    context['time_object'] = a
    print('start time' + str(a.start_time))
    print(a.hours)
    print(a.minutes)
    print('in display index')
    return render(request,'display/index.html', context=context)
