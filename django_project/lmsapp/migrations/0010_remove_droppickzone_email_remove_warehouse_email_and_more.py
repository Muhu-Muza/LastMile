# Generated by Django 4.2.1 on 2023-08-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0009_alter_package_deliverytype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='droppickzone',
            name='email',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='email',
        ),
        migrations.AlterField(
            model_name='droppickzone',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='droppickzone',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='droppickzone',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='droppickzone',
            name='tag',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='tag',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]