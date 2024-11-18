from django.urls import path

from users.views import Profile, Demande

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('Demande/', Demande, name='Demande')

]
