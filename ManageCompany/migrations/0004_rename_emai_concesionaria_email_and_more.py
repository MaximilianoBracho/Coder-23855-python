# Generated by Django 4.0 on 2022-01-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageCompany', '0003_rename_fecha_inscriocion_concesionaria_fecha_inscripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concesionaria',
            old_name='emai',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='concesionaria',
            name='fecha_inscripcion',
            field=models.DateField(verbose_name='1990-01-01'),
        ),
    ]
