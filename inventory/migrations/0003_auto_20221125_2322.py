# Generated by Django 3.2.8 on 2022-11-26 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20221125_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(default='null/foto.png', upload_to='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='null/foto.png', upload_to='Inventory'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='img',
            field=models.ImageField(default='null/foto.png', upload_to='SubCategory'),
        ),
    ]
