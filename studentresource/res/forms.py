# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange forms' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the forms, but don't rename db_table values or field names.
from django import forms
from django.forms import Textarea

from .models import *

class Admin(forms.Form):
    model = Admin
    fields = '__all__'
    widgets = {
        'body': Textarea()
    }



class Labfic(forms.Form):
    model = Labfic
    fields = '__all__'
    widgets = {
        'body': Textarea()
    }


class Labficsic(forms.Form):
    model = Labficsic
    fields = '__all__'
    widgets = {
        'body': Textarea()
    }




class Labsic(forms.Form):
    model = Labsic
    fields = '__all__'
    widgets = {
        'body': Textarea()
    }



class Recources(forms.Form):
    model = Recources
    fields = '__all__'
    widgets = {
        'body': Textarea()
    }



class Student(forms.Form):
    model = Student
    fields = '__all__'
    widgets = {
        'body': Textarea()
    }