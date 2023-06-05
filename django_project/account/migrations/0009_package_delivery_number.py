# Generated by Django 4.2.1 on 2023-06-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_package_delivery_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='delivery_number',
            field=models.CharField(default=12345, max_length=7, unique=True),
            preserve_default=False,
        ),
    ]