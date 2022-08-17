# Generated by Django 3.2.14 on 2022-08-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0009_alter_outcityobject_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incityobject',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='outcityobject',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='URL'),
        ),
    ]