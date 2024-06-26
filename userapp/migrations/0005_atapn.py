# Generated by Django 5.0.1 on 2024-04-03 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_atregdb_status'),
        ('userapp', '0004_psyapn'),
    ]

    operations = [
        migrations.CreateModel(
            name='atapn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('sub', models.CharField(max_length=40)),
                ('dte', models.DateField()),
                ('tme', models.TimeField()),
                ('status', models.IntegerField(default=0)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.atregdb')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.regdb')),
            ],
        ),
    ]
