# Generated by Django 5.0.4 on 2024-05-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shopId', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tk_shops',
            },
        ),
    ]