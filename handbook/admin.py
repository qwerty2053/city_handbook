from django.contrib import admin
from .models import Establishment, ImageSet, ContactInfo, Category, City


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'city')
    list_filter = ('category', 'city')
    search_fields = ('title', 'category', 'city')


@admin.register(ImageSet)
class ImageSetAdmin(admin.ModelAdmin):
    list_display = ('establishment', 'main_img')
    search_fields = ('establishment',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('establishment', 'phone', 'phone2', 'email')
    search_fields = ('establishment', 'phone', 'phone2', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'establishment_count')

    def establishment_count(self, instance):
        return instance.establishments.count()
    establishment_count.short_description = "Количество заведений"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'establishment_count')

    def establishment_count(self, instance):
        return instance.establishments.count()
    establishment_count.short_description = "Количество заведений"
