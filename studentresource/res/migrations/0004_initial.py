# Generated by Django 4.0.1 on 2022-01-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('res', '0003_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labfic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labroom', models.TextField(blank=True, null=True)),
                ('ficemail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'labfic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Labficsic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labroom', models.TextField(blank=True, null=True)),
                ('labname', models.TextField(blank=True, null=True)),
                ('dept', models.TextField(blank=True, null=True)),
                ('fic', models.TextField(blank=True, null=True)),
                ('ficemail', models.TextField(blank=True, null=True)),
                ('sic', models.TextField(blank=True, null=True)),
                ('sicemail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'labficsic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Labsic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labroom', models.TextField(blank=True, null=True)),
                ('sicemail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'labsic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(blank=True, max_length=100, null=True)),
                ('rname', models.CharField(blank=True, max_length=500, null=True)),
                ('descr', models.CharField(blank=True, max_length=500, null=True)),
                ('department', models.CharField(blank=True, max_length=500, null=True)),
                ('labroom', models.CharField(blank=True, max_length=500, null=True)),
                ('qty', models.CharField(blank=True, max_length=500, null=True)),
                ('installdate', models.CharField(blank=True, max_length=200, null=True)),
                ('issueto', models.CharField(blank=True, max_length=500, null=True)),
                ('issuedate', models.CharField(blank=True, max_length=500, null=True)),
                ('returndate', models.CharField(blank=True, max_length=500, null=True)),
                ('rtype', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('sicemail', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'recources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResAdmin',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('empid', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('dept', models.CharField(max_length=100)),
                ('extension', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'res_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('idno', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('studenttype', models.CharField(blank=True, max_length=100, null=True)),
                ('supervisorid', models.CharField(blank=True, max_length=100, null=True)),
                ('supervisorname', models.CharField(blank=True, db_column='SupervisorName', max_length=200, null=True)),
                ('cosupervisorid', models.CharField(blank=True, db_column='CosupervisorID', max_length=100, null=True)),
                ('cosupervisorname', models.CharField(blank=True, db_column='CosupervisorName', max_length=100, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]
