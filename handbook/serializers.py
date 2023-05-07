from rest_framework import serializers
from .models import Establishment, ContactInfo, ImageSet


class EstablishmentListSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Establishment
        fields = ('id', 'category', 'title', 'city')

    def get_city(self, instance):
        return instance.city.title

    def get_category(self, instance):
        return instance.category.title


class ImageSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageSet
        fields = ('main_img', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8')


class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInfo
        fields = ('phone', 'phone2', 'email')


class EstablishmentSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    contacts = ContactInfoSerializer()
    images = ImageSetSerializer()

    class Meta:
        model = Establishment
        fields = ('id', 'category', 'title', 'description', 'address', 'city', 'contacts', 'images')

    def get_city(self, instance):
        return instance.city.title

    def get_category(self, instance):
        return instance.category.title
