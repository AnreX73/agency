# Generated by Django 3.2.14 on 2022-08-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0015_auto_20220822_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcityobjecttype',
            name='in_main_page',
            field=models.BooleanField(default=True, verbose_name='в меню на главной странице'),
        ),
    ]