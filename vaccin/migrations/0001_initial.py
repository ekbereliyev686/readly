# Generated by Django 5.0.6 on 2024-05-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Vaccine Name')),
                ('description', models.TextField()),
                ('number_of_doses', models.IntegerField(default=1)),
                ('interval', models.IntegerField(default=0, help_text='Please provide the interval')),
                ('storage_temprature', models.IntegerField(blank=True, help_text='Please provide temperature', null=True)),
                ('minumum_age', models.IntegerField(default=0)),
            ],
        ),
    ]
