# Generated by Django 5.1.3 on 2025-02-07 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='wglasses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.wglasses'),
        ),
    ]
