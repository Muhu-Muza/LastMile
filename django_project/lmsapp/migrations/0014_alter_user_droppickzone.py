# Generated by Django 4.2.1 on 2023-07-05 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0013_alter_user_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DropPickZone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='lmsapp.droppickzone'),
        ),
    ]
