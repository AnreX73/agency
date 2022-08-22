# Generated by Django 3.2.14 on 2022-08-22 07:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0014_alter_graphics_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='incityobjecttype',
            name='in_main_page',
            field=models.BooleanField(default=True, verbose_name='в меню на главной странице'),
        ),
        migrations.AlterField(
            model_name='graphics',
            name='note',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='примечание'),
        ),
    ]