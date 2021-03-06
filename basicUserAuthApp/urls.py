from django.urls import path
from basicUserAuthApp import views
app_name = 'basicUserAuthApp'
urlpatterns = [
    path('login/',views.login_page, name='login_page'),
    path('registration/',views.registration, name='registration'),
    path('log_in/',views.log_in, name='log_in'),
    path('register/',views.register, name='register'),
    path('user_page/',views.user_page, name='user'),
]
