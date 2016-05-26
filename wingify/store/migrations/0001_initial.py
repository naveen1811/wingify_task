# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=500)),
                ('phone_no', models.CharField(max_length=10)),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('sku_id', models.CharField(db_index=True, max_length=128)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.OnlineStore')),
            ],
        ),
    ]