# Generated by Django 4.2.1 on 2023-07-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0027_package_gendertype_package_recipientidentification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='genderType',
            field=models.CharField(default=123456, max_length=200),
            preserve_default=False,
        ),
    ]
