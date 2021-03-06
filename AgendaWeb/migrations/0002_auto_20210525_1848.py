# Generated by Django 3.0.8 on 2021-05-25 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AgendaWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='dia',
            field=models.CharField(choices=[('sabado', 'sabado'), ('lunes', 'lunes'), ('viernes', 'viernes'), ('miercoles', 'miercoles'), ('martes', 'martes'), ('jueves', 'jueves')], default='lunes', max_length=11),
        ),
        migrations.AlterField(
            model_name='curso',
            name='estado',
            field=models.CharField(choices=[('cursada', 'cursada'), ('en proceso', 'proceso')], default='proceso', max_length=11),
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('curso', models.CharField(max_length=30)),
                ('semestre', models.CharField(choices=[('8', '8'), ('7', '3'), ('10', '10'), ('3', '3'), ('6', '6'), ('5', '5'), ('2', '2'), ('9', '9'), ('4', '4'), ('1', '1')], default='1', max_length=11)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pensumes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pensum',
                'verbose_name_plural': 'pensumes',
            },
        ),
    ]
