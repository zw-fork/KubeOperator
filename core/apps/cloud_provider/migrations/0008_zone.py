# Generated by Django 2.1.2 on 2019-07-31 10:10

import common.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_provider', '0007_auto_20190731_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('comment', models.CharField(blank=True, max_length=128, null=True, verbose_name='Comment')),
                ('vars', common.models.JsonDictTextField(default={})),
                ('cloud_zone', models.CharField(default=None, max_length=128, null=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud_provider.Region')),
            ],
        ),
    ]
