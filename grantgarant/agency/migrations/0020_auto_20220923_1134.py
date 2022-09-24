# Generated by Django 3.2.14 on 2022-09-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0019_auto_20220907_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incityobject',
            name='is_for_rent',
        ),
        migrations.RemoveField(
            model_name='incityobject',
            name='is_for_sale',
        ),
        migrations.AddField(
            model_name='incityobject',
            name='sale_or_rent',
            field=models.CharField(choices=[('s', 'sale'), ('r', 'rent')], default='s', max_length=25),
        ),
    ]