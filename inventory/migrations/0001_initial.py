# Generated by Django 3.2.8 on 2022-11-26 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('img', models.ImageField(upload_to='Categories')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('img', models.ImageField(upload_to='Categories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('tax', models.FloatField(default=0)),
                ('quanty', models.FloatField(default=1)),
                ('description', models.TextField()),
                ('shipping', models.FloatField(default=0)),
                ('img', models.ImageField(upload_to='Inventory')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.subcategories')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_1', models.ImageField(upload_to='Gallery')),
                ('img_2', models.ImageField(upload_to='Gallery')),
                ('img_3', models.ImageField(upload_to='Gallery')),
                ('img_4', models.ImageField(upload_to='Gallery')),
                ('img_5', models.ImageField(upload_to='Gallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('size', models.CharField(choices=[('ninguno', 'ninguno'), ('xs', 'xs'), ('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl'), ('xxxl', 'xxxl')], max_length=10)),
                ('state', models.CharField(choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')], max_length=8)),
                ('marca', models.CharField(blank=True, max_length=40, null=True)),
                ('modelo', models.CharField(blank=True, max_length=40, null=True)),
                ('unidades_por_pack', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
