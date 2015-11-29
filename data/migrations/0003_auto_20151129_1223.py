# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20151129_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='culture',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='evening',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='leisure',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='man',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='morning',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='noon',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='restaurant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='shopping',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='woman',
            field=models.IntegerField(default=0),
        ),
    ]
