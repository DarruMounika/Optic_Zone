# Generated by Django 5.1.3 on 2025-02-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_wglasses'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
