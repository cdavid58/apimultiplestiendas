# Generated by Django 3.2.8 on 2022-11-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_features_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='img_1',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img_4',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img_5',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
    ]