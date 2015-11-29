from django.contrib import admin
from data.models import Venue, Tag, VenueToTag


class VenueToTagInline(admin.StackedInline):
    model = VenueToTag

class VenueAdmin(admin.ModelAdmin):
    inlines = [
        VenueToTagInline,
    ]


admin.site.register(Venue, VenueAdmin)
admin.site.register(Tag)
admin.site.register(VenueToTag)
