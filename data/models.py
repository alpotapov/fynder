from django.db import models


class Venue (models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    image_url_original = models.CharField(max_length=255, blank=True, default='')
    rating = models.IntegerField()

    price_range = models.IntegerField()

    yelp_id = models.CharField(max_length=255, blank=True, default='')

    country_code = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=255, blank=True, default='')
    postal_code = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    lat = models.CharField(max_length=255, blank=True, default='')
    lon = models.CharField(max_length=255, blank=True, default='')

    categories = models.ManyToManyField('Category')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    woman = models.IntegerField(default=0)
    man = models.IntegerField(default=0)
    morning = models.IntegerField(default=0)
    noon = models.IntegerField(default=0)
    evening = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    leisure = models.IntegerField(default=0)
    shopping = models.IntegerField(default=0)
    restaurant = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def as_array(self):
        return [
            self.woman, self.man, self.morning, self.noon, self.evening, self.culture, self.leisure, self.shopping, self.restaurant
        ]
