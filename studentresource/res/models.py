# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    empid = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Labfic(models.Model):
    labroom = models.TextField(blank=True, null=True)
    ficemail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labfic'


class Labficsic(models.Model):
    labroom = models.TextField(blank=True, null=True)
    labname = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    fic = models.TextField(blank=True, null=True)
    ficemail = models.TextField(blank=True, null=True)
    sic = models.TextField(blank=True, null=True)
    sicemail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labficsic'


class Labsic(models.Model):
    labroom = models.TextField(blank=True, null=True)
    sicemail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labsic'


class Recources(models.Model):
    rid = models.CharField(max_length=100, blank=True, null=True)
    rname = models.CharField(max_length=500, blank=True, null=True)
    descr = models.CharField(max_length=500, blank=True, null=True)
    department = models.CharField(max_length=500, blank=True, null=True)
    labroom = models.CharField(max_length=500, blank=True, null=True)
    qty = models.CharField(max_length=500, blank=True, null=True)
    installdate = models.CharField(max_length=200, blank=True, null=True)
    issueto = models.CharField(max_length=500, blank=True, null=True)
    issuedate = models.CharField(max_length=500, blank=True, null=True)
    returndate = models.CharField(max_length=500, blank=True, null=True)
    rtype = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    sicemail = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recources'


class Student(models.Model):
    idno = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    studenttype = models.CharField(max_length=100, blank=True, null=True)
    supervisorid = models.CharField(max_length=100, blank=True, null=True)
    supervisorname = models.CharField(db_column='SupervisorName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cosupervisorid = models.CharField(db_column='CosupervisorID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cosupervisorname = models.CharField(db_column='CosupervisorName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.username

    empAuth_objects = models.Manager()
