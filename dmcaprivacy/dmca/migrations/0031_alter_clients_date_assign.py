# Generated by Django 3.2 on 2021-09-21 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0030_auto_20210921_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_assign',
            field=models.DateField(default=datetime.datetime(2021, 10, 22, 19, 37, 46, 553662)),
        ),
    ]
