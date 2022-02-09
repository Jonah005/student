
from . import views
from django.urls import path, include
urlpatterns = [
    path('', views.login),
    path('user_login/',views.studlogin,name='user_login/'),

]
