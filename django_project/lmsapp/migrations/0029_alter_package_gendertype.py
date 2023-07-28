# Generated by Django 4.2.1 on 2023-07-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0028_alter_package_gendertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='genderType',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20, verbose_name='Role'),
        ),
    ]
