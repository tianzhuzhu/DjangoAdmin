# Generated by Django 2.2.4 on 2021-07-17 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myoperations', '0005_auto_20210717_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 17, 17, 23, 422551), verbose_name='操作时间'),
        ),
    ]
