from django.db import models


class Venue (models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    image_url_original = models.CharField(max_length=255, blank=True, default='')
    rating = models.IntegerField()

    price_range = models.IntegerField()

    yelp_id = models.IntegerField()

    country_code = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=255, blank=True, default='')
    postal_code = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    lat = models.CharField(max_length=255, blank=True, default='')
    lon = models.CharField(max_length=255, blank=True, default='')


class VenueToTag(models.Model):
    venue = models.ForeignKey('Venue')
    tag = models.ForeignKey('Tag')
    weight = models.IntegerField()


class Tag (models.Model):
    name = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return self.name