# Generated by Django 4.2.1 on 2023-07-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0018_droppickzone_latitude_droppickzone_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='sender_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='sender_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
