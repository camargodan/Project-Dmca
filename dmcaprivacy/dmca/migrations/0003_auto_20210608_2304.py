# Generated by Django 3.2 on 2021-06-09 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dmca', '0002_remove_clients_imag_clie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='worker_id_work',
        ),
        migrations.AddField(
            model_name='clients',
            name='worker_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_worker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clients',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Workers',
        ),
    ]
