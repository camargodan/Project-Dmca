# Generated by Django 3.2 on 2021-07-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210705_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='assign',
            field=models.BooleanField(default=False),
        ),
    ]
