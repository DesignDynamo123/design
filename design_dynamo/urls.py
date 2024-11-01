from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('contact',views.contact, name = 'contact'),
    path('graphic',views.graphic, name = 'graphic'),
    path('teaser',views.teaser, name = 'teaser'),
    path('CGI',views.cgi, name = 'CGI'),
    path('team',views.team, name = 'team'),
    path('submit_query', views.submit_query, name='submit_query'),
    path('home',views.home, name = 'home'),
]