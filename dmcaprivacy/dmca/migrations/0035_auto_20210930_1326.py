# Generated by Django 3.2 on 2021-09-30 17:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0034_auto_20210927_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tubereports',
            name='stat_tube',
        ),
        migrations.AddField(
            model_name='tubereports',
            name='cant_urls',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tubereports',
            name='id_tube_pages',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dmca.tubepages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tubereports',
            name='tube_urls',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='date_assign',
            field=models.DateField(default=datetime.datetime(2021, 10, 31, 13, 24, 32, 406952)),
        ),
        migrations.AlterField(
            model_name='tubereports',
            name='clients_id_clie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmca.clients'),
        ),
        migrations.DeleteModel(
            name='TubeHasPages',
        ),
    ]
