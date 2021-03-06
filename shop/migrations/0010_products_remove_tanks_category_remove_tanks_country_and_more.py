# Generated by Django 4.0.1 on 2022-02-13 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_fuel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('discription', models.TextField(blank=True, max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category_tanks')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.country')),
            ],
        ),
        migrations.RemoveField(
            model_name='tanks',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tanks',
            name='country',
        ),
        migrations.DeleteModel(
            name='Fuel',
        ),
        migrations.DeleteModel(
            name='Tanks',
        ),
    ]
