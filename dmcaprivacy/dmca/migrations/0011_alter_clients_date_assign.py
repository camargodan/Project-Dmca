# Generated by Django 3.2 on 2021-08-04 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0010_auto_20210803_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_assign',
            field=models.DateField(default=datetime.datetime(2021, 9, 4, 19, 28, 9, 273455)),
        ),
    ]
