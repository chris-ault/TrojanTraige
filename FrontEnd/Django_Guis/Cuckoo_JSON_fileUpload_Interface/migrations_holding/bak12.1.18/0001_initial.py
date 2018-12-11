# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dlltable',
            fields=[
                ('malware_dll_id', models.SmallIntegerField()),
                ('dll_name', models.CharField(max_length=80, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'dlltable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('severity', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('os', models.CharField(blank=True, db_column=b'OS', max_length=255, null=True)),
                ('categoryid', models.CharField(blank=True, db_column=b'CategoryID', max_length=255, null=True)),
                ('rollupstatus', models.CharField(blank=True, db_column=b'Rollupstatus', max_length=255, null=True)),
                ('schemaversion', models.CharField(blank=True, db_column=b'Schemaversion', max_length=255, null=True)),
                ('date', models.CharField(blank=True, db_column=b'Date', max_length=255, null=True)),
                ('threatid', models.BigIntegerField(blank=True, db_column=b'threatID', null=True)),
                ('hash', models.CharField(db_column=b'HASH', max_length=32, primary_key=True, serialize=False)),
                ('unpackedmd5', models.CharField(blank=True, db_column=b'unpackedMD5', max_length=32, null=True)),
                ('location', models.CharField(blank=True, db_column=b'Location', max_length=255, null=True)),
                ('subtype', models.CharField(blank=True, db_column=b'subType', max_length=255, null=True)),
            ],
            options={
                'db_table': 'element',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Malware',
            fields=[
                ('severity', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('os', models.CharField(blank=True, db_column=b'OS', max_length=255, null=True)),
                ('categoryid', models.CharField(blank=True, db_column=b'CategoryID', max_length=255, null=True)),
                ('rollupstatus', models.CharField(blank=True, db_column=b'Rollupstatus', max_length=255, null=True)),
                ('schemaversion', models.CharField(blank=True, db_column=b'Schemaversion', max_length=255, null=True)),
                ('date', models.CharField(blank=True, db_column=b'Date', max_length=255, null=True)),
                ('threatid', models.BigIntegerField(blank=True, db_column=b'threatID', null=True)),
                ('hash', models.CharField(db_column=b'Hash', max_length=32, primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, db_column=b'Location', max_length=255, null=True)),
                ('subtype', models.CharField(blank=True, db_column=b'subType', max_length=255, null=True)),
                ('filetype', models.CharField(blank=True, db_column=b'filetype', max_length=255, null=True)),
            ],
            options={
                'db_table': 'malware',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Malware2Dll',
            fields=[
                ('hash', models.CharField(db_column=b'Hash', max_length=32, primary_key=True, serialize=False)),
                ('malware_dll_id', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'malware2dll',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=b'documents/')),
            ],
        ),
    ]