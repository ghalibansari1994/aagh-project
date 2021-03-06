# Generated by Django 2.1.1 on 2018-09-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DESKTOP', 'DESKTOP'), ('LAPTOP', 'Laptop'), ('ACCESSORIES', 'Accessories'), ('HARDWARE', 'Hardware'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
