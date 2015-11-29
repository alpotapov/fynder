# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20151129_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='venue',
        ),
        migrations.AddField(
            model_name='venue',
            name='categories',
            field=models.ManyToManyField(to='data.Category'),
        ),
    ]
