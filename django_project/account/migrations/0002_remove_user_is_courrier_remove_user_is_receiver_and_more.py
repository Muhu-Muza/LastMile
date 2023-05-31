# Generated by Django 4.2.1 on 2023-05-31 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_courrier',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_receiver',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_sender',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('courier', 'courier'), ('sender', 'sender'), ('receiver', 'reciever')], default='sender', max_length=10, verbose_name='role'),
        ),
    ]
