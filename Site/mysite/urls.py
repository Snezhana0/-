from django.urls import path, include

from django.contrib import admin
from .views import *

urlpatterns = [
    path('',index, name ='home'),
    path('game/', game, name='game'),
    path('about/', about, name = 'about'),
    path('faq/', faq, name = 'faq'),
    path('contact/', contact, name = 'contact'),
    path('ind/', ind, name = 'ind'),
    path('admin/', admin.site.urls, name='admin'),
    path('login', loginPage, name = 'login'),
    path('register', registerPage, name='register'),
    path('logout', doLogout, name='logout'),
    path('shrek/', shrek, name='shrek'),
    path('test/', test, name='test'),
    path('twin/', twin, name='twin'),
    path('depeche/', depeche, name='depeche'),
    path('bowie/', bowie, name='bowie'),
    path('lana/', lana, name='lana'),

]