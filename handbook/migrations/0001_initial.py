# Generated by Django 4.2.1 on 2023-05-07 17:31

from django.db import migrations, models
import django.db.models.deletion
import handbook.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handbook.category', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handbook.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведения',
            },
        ),
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(upload_to=handbook.models.generate_image_path, verbose_name='Главная фотография')),
                ('img2', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #2')),
                ('img3', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #3')),
                ('img4', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #4')),
                ('img5', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #5')),
                ('img6', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #6')),
                ('img7', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #7')),
                ('img8', models.ImageField(blank=True, upload_to=handbook.models.generate_image_path, verbose_name='Фотография #8')),
                ('establishment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='handbook.establishment')),
            ],
            options={
                'verbose_name': 'Фотографии',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('phone2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Доп. телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('establishment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='handbook.establishment')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]