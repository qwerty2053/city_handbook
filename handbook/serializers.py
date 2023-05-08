from rest_framework import serializers
from .models import Establishment, ContactInfo, ImageSet, City, Category


class CityWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('title',)


class CategoryWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ImageSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageSet
        fields = ('main_img', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8')


class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInfo
        fields = ('phone', 'phone2', 'email')


class EstablishmentSerializer(serializers.ModelSerializer):
    contacts = ContactInfoSerializer()
    images = ImageSetSerializer()
    city = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Establishment
        fields = ('id', 'category', 'title', 'description', 'address', 'city', 'contacts', 'images')

    def get_city(self, instance):
        return instance.city.title

    def get_category(self, instance):
        return instance.category.title


class EstablishmentListSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Establishment
        fields = ('id', 'title', 'category', 'city')

    def get_city(self, instance):
        return instance.city.title

    def get_category(self, instance):
        return instance.category.title
