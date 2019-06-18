from django.urls import path
from basicUserAuthApp import views
app_name = 'basicUserAuthApp'
urlpatterns = [
    path('login/',views.login, name='login'),
    path('registration/',views.registration, name='registration'),
    path('log_in/',views.log_in, name='log_in'),
    path('register/',views.register, name='register'),
]
