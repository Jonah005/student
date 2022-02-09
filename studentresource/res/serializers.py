from rest_framework import serializers
from .models import *
from bootstrap_modal_forms.forms import BSModalModelForm

class AdminSerializer(BSModalModelForm):
    class Meta:
        model = Admin
        fields = ('empid',
                  'password',
                  'name',
                  'dept',
                  'extension',
                  'mobile')

class LabficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labfic
        fields = ('labroom',
                  'ficemail')

class LabficsicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labficsic
        fields = ('labroom',
                  'labname',
                  'dept',
                  'fic',
                  'ficemail',
                  'sic',
                  'sicemail')

class LabsicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labsic
        fields = ('labroom',
                  'sicemail')

class RecourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recources
        fields = ('rid',
                  'rname',
                  'descr',
                  'department',
                  'labroom',
                  'qty',
                  'installdate',
                  'issueto',
                  'issuedate',
                  'returndate',
                  'rtype',
                  'status',
                  'sicemail')



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('idno',
                  'password',
                  'name',
                  'department',
                  'studenttype',
                  'supervisorid',
                  'supervisorname',
                  'cosupervisorid',
                  'cosupervisorname')
