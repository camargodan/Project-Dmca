# Generated by Django 3.2 on 2021-06-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmca', '0005_auto_20210623_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='name_page',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='tubepages',
            name='name_tube_page',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]
