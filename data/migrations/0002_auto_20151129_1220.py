# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, blank=True)),
                ('woman', models.IntegerField()),
                ('man', models.IntegerField()),
                ('morning', models.IntegerField()),
                ('noon', models.IntegerField()),
                ('evening', models.IntegerField()),
                ('culture', models.IntegerField()),
                ('leisure', models.IntegerField()),
                ('shopping', models.IntegerField()),
                ('restaurant', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='venuetotag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='venuetotag',
            name='venue',
        ),
        migrations.AlterField(
            model_name='venue',
            name='yelp_id',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='VenueToTag',
        ),
        migrations.AddField(
            model_name='category',
            name='venue',
            field=models.ForeignKey(to='data.Venue'),
        ),
    ]
