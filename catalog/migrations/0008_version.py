# Generated by Django 5.0.3 on 2024-05-04 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_blogpost_number_of_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_version', models.PositiveIntegerField(verbose_name='Номер версии продукта')),
                ('name_of_versions', models.CharField(max_length=150, verbose_name='Название версии')),
                ('is_active_version', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
