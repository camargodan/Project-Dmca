# Generated by Django 3.2 on 2021-08-03 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0007_tubepages_contact_tube'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='data_assign',
            field=models.DateField(default=datetime.datetime(2021, 9, 3, 10, 59, 25, 946937)),
        ),
    ]
