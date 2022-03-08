from multiprocessing import context
from django.shortcuts import redirect, render
from .models import announcement,Reservation
from .forms import announcementForm,ReservationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    ''' The Home page '''
    return render(request,'IM/index.html')


@login_required
def announcements(request):
    ''' Show all announcements '''
    announcements = announcement.objects.order_by('date_added')
    context = {'announcements':announcements}
    return render(request,'IM/announcements.html',context)


def add_announcements(request):
    ''' Add an entry '''
    if request.method != 'POST':
        ''' No date submitted '''
        form = announcementForm()
    else:
        ''' Post data submitted '''
        form = announcementForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('IM:announcements')
    ''' Display a blank or invalid form '''
    context = {'form':form}
    return render(request,'IM/add_announcements.html',context)


def reservations(request):
    ''' Show all reservations '''
    reservations = Reservation.objects.order_by('date')
    context = {'reservations':reservations}
    return render(request,'IM/reservations.html',context)


def add_reservations(request):
    ''' Add a reservation '''
    if request.method != 'POST':
        ''' No date submitted '''
        form = ReservationForm()
    else:
        ''' Post data submitted '''
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('IM:reservations')
    ''' Display a blank or invalid form '''
    return render(request,'IM/add_reservations.html',{'form':form})

    