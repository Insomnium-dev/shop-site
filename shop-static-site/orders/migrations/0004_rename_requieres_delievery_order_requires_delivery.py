# Generated by Django 5.1.6 on 2025-02-17 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_requires_delivery_order_requieres_delievery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='requieres_delievery',
            new_name='requires_delivery',
        ),
    ]
