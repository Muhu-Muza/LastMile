# Generated by Django 4.2.1 on 2023-07-17 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0021_user_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='token',
            new_name='verification_token',
        ),
    ]