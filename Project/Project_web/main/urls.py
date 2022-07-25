from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news_home'),
    path('about', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),

    path('friends', views.friends, name='friends'),
    path('messenger', views.messenger, name='messenger'),
    path('profile', views.profile, name='profile'),
    path('support', views.support, name='support'),
]
