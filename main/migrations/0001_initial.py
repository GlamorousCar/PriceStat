# Generated by Django 3.1.5 on 2021-01-11 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=512)),
                ('biggest', models.TextField(default='no-image.png')),
                ('large', models.TextField(default='no-image.png')),
                ('medium', models.TextField(default='no-image.png')),
                ('small', models.TextField(default='no-image.png')),
                ('weight', models.IntegerField()),
                ('slug', models.SlugField(default='slug', max_length=256, unique=True)),
                ('description', models.TextField()),
                ('composition', models.TextField(default='Состав')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='RootCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PriceCheanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('old_price', models.DecimalField(decimal_places=2, default=100.0, max_digits=9, verbose_name='Цена')),
                ('price', models.DecimalField(decimal_places=2, default=100.0, max_digits=9, verbose_name='Цена по скидке')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='root_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.rootcategory', verbose_name='Родительская категория'),
        ),
    ]
