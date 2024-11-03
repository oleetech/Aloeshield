# Generated by Django 5.1.1 on 2024-10-30 10:52

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_product_alter_color_color_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.AlterField(
            model_name='product',
            name='range',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Range'),
        ),
        migrations.AlterField(
            model_name='product',
            name='technical_data',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Technical Data'),
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, to='website.color'),
        ),
    ]
