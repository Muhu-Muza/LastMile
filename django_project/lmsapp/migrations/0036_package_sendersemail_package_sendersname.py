# Generated by Django 4.2.1 on 2023-08-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0035_package_completed_at_package_received_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='sendersEmail',
            field=models.CharField(default=12345678, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='sendersName',
            field=models.CharField(default=1234567, max_length=200),
            preserve_default=False,
        ),
    ]