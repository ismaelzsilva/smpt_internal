# Generated by Django 4.1.5 on 2023-01-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricationorders',
            name='fabrication_order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fabricationorders',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
