from django.contrib import admin
from data.models import Venue, Category


# class CategoryInline(admin.StackedInline):
#     model = Category
#
#
# class VenueAdmin(admin.ModelAdmin):
#     inlines = [
#         CategoryInline,
#     ]


admin.site.register(Venue)
admin.site.register(Category)