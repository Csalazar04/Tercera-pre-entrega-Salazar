# Generated by Django 4.1.5 on 2023-01-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantSemestres', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]
