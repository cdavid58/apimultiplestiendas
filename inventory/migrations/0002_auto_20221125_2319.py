# Generated by Django 3.2.8 on 2022-11-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(default='foto.png', upload_to='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='foto.png', upload_to='Inventory'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='img',
            field=models.ImageField(default='foto.png', upload_to='SubCategory'),
        ),
    ]
