# Generated by Django 5.1.1 on 2024-11-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_projectcategory_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color_description',
            field=models.TextField(default='No color description available'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color_code',
            field=models.CharField(blank=True, default=None, max_length=7, null=True),
        ),
    ]