from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http.response import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import *

from rest_framework.decorators import api_view
from django.urls import path
from bootstrap_modal_forms.generic import BSModalCreateView
import mysql.connector
from mysql.connector import Error

def login(request):

    return render(request, 'login.html')

def studlogin(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        print(request.POST)
        if username!="jake":
            print("No")

        """user = Student.empAuth_objects.get(name=username, password=password)
        print(user)
        try:
            user = Student.empAuth_objects.get(name=username, password=password)
            if user is not None:
                return render(request, 'login.html')
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))

                return render(request, 'login.html')
        except Exception as identifier:

            return render(request, 'login.html')

    else:
        return render(request, 'index.html')
"""

def studlogin(request):
    return render(request, 'index.html')
