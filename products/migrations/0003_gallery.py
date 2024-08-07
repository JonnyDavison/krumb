# Generated by Django 5.0.4 on 2024-07-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
