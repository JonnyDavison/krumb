# Generated by Django 5.0.4 on 2024-05-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('bg-1', '1'), ('bg-2', '2'), ('bg-3', '3'), ('bg-4', '4'), ('bg-5', '5'), ('bg-6', '6')], max_length=4, null=True),
        ),
    ]
