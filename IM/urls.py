""" Defines URLs for this app """
from django.urls import path
from . import views

app_name = 'IM'
urlpatterns=[
    # Home page
    path('',views.index,name='index'),
    # Announcements page
    path('announcements/',views.announcements,name='announcements'),
    # Add an announcement page
    path('add_announcements/',views.add_announcements,name='add_announcements'),
    # Reservations page
    path('reservations/',views.reservations,name='reservations'),
    # Add a reservation
    path('add_reservations/',views.add_reservations,name='add_reservations')
]