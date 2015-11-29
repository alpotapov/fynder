# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, blank=True)),
                ('image_url_original', models.CharField(default=b'', max_length=255, blank=True)),
                ('rating', models.IntegerField()),
                ('price_range', models.IntegerField()),
                ('yelp_id', models.IntegerField()),
                ('country_code', models.CharField(default=b'', max_length=255, blank=True)),
                ('city', models.CharField(default=b'', max_length=255, blank=True)),
                ('postal_code', models.CharField(default=b'', max_length=255, blank=True)),
                ('address', models.CharField(default=b'', max_length=255, blank=True)),
                ('lat', models.CharField(default=b'', max_length=255, blank=True)),
                ('lon', models.CharField(default=b'', max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenueToTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField()),
                ('tag', models.ForeignKey(to='data.Tag')),
                ('venue', models.ForeignKey(to='data.Venue')),
            ],
        ),
    ]
