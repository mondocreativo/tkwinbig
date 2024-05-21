# Generated by Django 5.0.4 on 2024-05-21 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('shops', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('1', '未启动'), ('2', '正在进行'), ('3', '已完成')], default='1', max_length=1)),
                ('match_quantity', models.IntegerField(null=True)),
                ('willing_quantity', models.IntegerField(null=True)),
                ('send_quantity', models.IntegerField(null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'tk_tasks',
            },
        ),
    ]
