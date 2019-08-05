from django.shortcuts import render
from control.models import clarification, time
from django.views.decorators.csrf import csrf_exempt
import time as ti 
# Create your views here.


def index(request):
    "View for main control page"

    context={}
    for item in clarification.objects.all():
        item.delete()
    for item in time.objects.all():
        item.delete()
    a = time(hours=0,minutes=0,start_time=0)
    a.save()
    context['time_object'] = a
    context['start_bool'] = False
    context['hours'], context['minutes'] = 0, 0
    return render(request, 'control/index.html', context=context)

def receive(request):
    if request.method == 'POST':
        new = clarification(my_message=request.POST['enter'])
        print(new.my_message + 'hello')
        new.save()
        context = {'messages': messages_helper}
    a = time.objects.all()
    context['start_bool'] = False

    if a:
        a = a.first()
        context['time_object']=a
        context['hours'], context['minutes'] = a.hours, a.minutes
    else:
        context['hours'], context['minutes'] = 0, 0
    print(context)

    print('in receive')
    return render(request, 'control/index.html', context=context)

@csrf_exempt
def delete(request):

    context={}
    if request.method == 'POST':
        which = request.POST['which']
        for item in clarification.objects.all():
            print(item.my_message, which)
            if item.my_message == which:
                item.delete()
                break;

    context = {'messages': messages_helper()}
    context['start_bool'] = False
    a = time.objects.all().first()
    context['time_object']=a
    context['start_time'] = a.start_time
    context['hours'], context['minutes'] = a.hours, a.minutes
    print(context)
    print('in delete')
    return render(request, 'control/index.html', context=context)


def time_response(request):
    if request.method == 'POST':
        remaining_time = request.POST['time_enter']
        input_time = remaining_time.split(':')
        input_time = [int(x) for x in input_time]
        ob = time.objects.all().first()
        ob.hours = input_time[0]
        ob.minutes = input_time[1]
        ob.save(update_fields=['hours','minutes'])

    context = {'messages': messages_helper()}
    context['time_object'] = ob
    context['start_time'] = ob.start_time
    context['start_bool'] = False
    context['hours'], context['minutes'] = ob.hours, ob.minutes
    print(context)
    print('in time_response')
    return render(request, 'control/index.html', context=context)

def start(request):
    a = ti.time()
    context = {'messages': messages_helper()}
    b = time.objects.all().first()
    if b.start_time == 0:
        b.start_time = int(a*1000)
        b.save(update_fields=['start_time'])
        context['hours'], context['minutes'] = b.hours, b.minutes
        context['start_time'] = a
        context['start_bool'] = True
    else:
        context['start_time'] = b.start_time
        context['start_bool'] = True
        context['hours'], context['minutes'] = 0, 0

    context['time_object']=b
    print(b.start_time)
    print('in start')
    return render(request, 'control/index.html', context=context)

def messages_helper():
    lst = []
    for item in clarification.objects.all():
        lst.append(item.my_message[:])
    return lst
