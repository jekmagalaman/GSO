# Generated by Django 5.2.4 on 2025-07-10 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaterialUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_used', models.PositiveIntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.material')),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.servicerequest')),
            ],
        ),
    ]
