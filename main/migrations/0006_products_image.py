# Generated by Django 5.1.6 on 2025-05-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_products_product_external_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
