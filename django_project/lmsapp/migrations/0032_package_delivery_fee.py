# Generated by Django 4.2.1 on 2023-07-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0031_alter_package_gendertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='delivery_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
