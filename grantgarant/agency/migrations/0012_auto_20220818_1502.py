# Generated by Django 3.2.14 on 2022-08-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0011_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='название')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='описание если есть')),
                ('extra_description', models.TextField(blank=True, verbose_name='описание дополнительное')),
            ],
            options={
                'verbose_name': 'контактную информацию',
                'verbose_name_plural': 'Контакты',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='graphics',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
    ]