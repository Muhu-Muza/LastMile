# Generated by Django 4.2.1 on 2023-06-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_rename_delivery_number_package_package_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tag',
            field=models.CharField(default=123456, max_length=20),
            preserve_default=False,
        ),
    ]
