# Generated by Django 3.2 on 2021-07-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_user_imag_clie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(default=True, help_text='Designates that this user has the permissions to access to Worker module.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_worker',
            field=models.BooleanField(default=False, help_text='Designates that this user has the permissions to access to Client module.'),
        ),
    ]
