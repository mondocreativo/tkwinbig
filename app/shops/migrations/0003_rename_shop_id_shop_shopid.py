# Generated by Django 5.0.4 on 2024-05-07 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_rename_create_at_shop_createat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shop_id',
            new_name='shopId',
        ),
    ]