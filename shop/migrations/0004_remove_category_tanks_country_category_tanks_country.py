# Generated by Django 4.0.1 on 2022-01-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_tanks_country_tanks_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_tanks',
            name='Country',
        ),
        migrations.AddField(
            model_name='category_tanks',
            name='Country',
            field=models.ManyToManyField(to='shop.Country'),
        ),
    ]
