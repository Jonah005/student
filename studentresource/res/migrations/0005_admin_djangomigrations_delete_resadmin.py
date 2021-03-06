# Generated by Django 4.0.1 on 2022-01-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(blank=True, max_length=500, null=True)),
                ('password', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('dept', models.CharField(blank=True, max_length=100, null=True)),
                ('extension', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='ResAdmin',
        ),
    ]
