# Generated by Django 4.0.1 on 2022-02-13 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_products_remove_tanks_category_remove_tanks_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('discription', models.TextField(blank=True, max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tanks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('discription', models.TextField(blank=True, max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category_tanks')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.country')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='fuel',
            name='category',
            field=models.ManyToManyField(to='shop.Tanks'),
        ),
    ]
