# Generated by Django 4.0 on 2022-01-19 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageCompany', '0004_rename_emai_concesionaria_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empelado',
            new_name='Empleado',
        ),
    ]