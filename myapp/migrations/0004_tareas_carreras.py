# Generated by Django 4.1.5 on 2023-01-21 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_cantsemestres_carreras_semestres'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='carreras',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Carreras', to='myapp.carreras'),
        ),
    ]
