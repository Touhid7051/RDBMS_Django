# Generated by Django 3.1 on 2020-11-30 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RDBMS_app', '0002_oder_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
    ]
