# Generated by Django 3.2 on 2021-05-18 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0006_alter_user_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
