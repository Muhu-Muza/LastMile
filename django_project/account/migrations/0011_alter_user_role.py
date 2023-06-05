
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_rename_packagedescripton_package_packagedescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('courier', 'courier'), ('sender', 'sender'), ('recipient', 'recipient')], max_length=10, verbose_name='role'),
        ),
    ]
