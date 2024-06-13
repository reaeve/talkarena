# Generated by Django 5.0.1 on 2024-04-12 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_psyapn_rid'),
    ]

    operations = [
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.CharField(max_length=50)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.regdb')),
            ],
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=1000)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.topic')),
            ],
        ),
    ]
