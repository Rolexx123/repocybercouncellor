# Generated by Django 5.1.3 on 2024-11-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councellor', '0002_rename_district_councellor_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=30, null=True)),
                ('rating', models.CharField(blank=True, max_length=30, null=True)),
                ('feedback', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]