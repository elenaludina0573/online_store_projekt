# Generated by Django 5.0.3 on 2024-04-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_contactsdata_contacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='number_of_views',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
