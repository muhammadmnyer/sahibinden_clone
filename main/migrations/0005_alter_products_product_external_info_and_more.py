# Generated by Django 5.1.6 on 2025-05-02 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_subcategorieschildparentrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_external_info',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ProductsSubcategoriesChildParentRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
                ('subcategories_linked_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategorieschildparentrelation')),
            ],
        ),
    ]
