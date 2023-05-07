from django.contrib import admin
from .models import Establishment, ImageSet, ContactInfo, Category, City


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'city')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'city')
    search_fields = ('title', 'category', 'city')


admin.site.register(ImageSet)
admin.site.register(ContactInfo)
admin.site.register(Category)
admin.site.register(City)
