# Generated by Django 3.2.14 on 2022-08-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_alter_incityobject_balcony'),
    ]

    operations = [
        migrations.AddField(
            model_name='incityobject',
            name='slug',
            field=models.SlugField(default='no_slug', max_length=150, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='outcityobject',
            name='slug',
            field=models.SlugField(default='no_slug', max_length=150, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='graphics',
            name='note',
            field=models.CharField(blank=True, max_length=55, verbose_name='примечание'),
        ),
    ]
