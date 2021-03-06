# Generated by Django 4.0.1 on 2022-02-03 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_tanks_category_tanks_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_tanks',
            name='Country',
        ),
        migrations.AddField(
            model_name='tanks',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.country'),
        ),
        migrations.RemoveField(
            model_name='tanks',
            name='category',
        ),
        migrations.AddField(
            model_name='tanks',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category_tanks'),
        ),
    ]
