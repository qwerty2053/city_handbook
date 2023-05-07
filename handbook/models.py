from django.db import models
import uuid


def generate_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"{instance.establishment.id}/{uuid.uuid4()}.{ext}"


class ImageSet(models.Model):
    establishment = models.OneToOneField("handbook.establishment", related_name='images', on_delete=models.CASCADE)
    main_img = models.ImageField(upload_to=generate_image_path, verbose_name='Главная фотография')
    img2 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #2', blank=True)
    img3 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #3', blank=True)
    img4 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #4', blank=True)
    img5 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #5', blank=True)
    img6 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #6', blank=True)
    img7 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #7', blank=True)
    img8 = models.ImageField(upload_to=generate_image_path, verbose_name='Фотография #8', blank=True)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.establishment.title


class City(models.Model):
    title = models.CharField('Название', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Название', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    phone2 = models.CharField('Доп. телефон', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='Почта')
    establishment = models.OneToOneField("handbook.establishment", related_name='contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.establishment.title


class Establishment(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=50)
    category = models.ForeignKey('handbook.category', on_delete=models.CASCADE, verbose_name='Категория')
    city = models.ForeignKey('handbook.city', on_delete=models.CASCADE, verbose_name='Город')

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'

    def __str__(self):
        return self.title
