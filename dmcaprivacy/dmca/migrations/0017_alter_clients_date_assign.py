# Generated by Django 3.2 on 2021-09-07 00:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0016_alter_clients_date_assign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_assign',
            field=models.DateField(default=datetime.datetime(2021, 10, 7, 20, 57, 31, 61897)),
        ),
    ]
