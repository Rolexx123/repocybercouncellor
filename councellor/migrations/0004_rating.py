# Generated by Django 5.1.3 on 2024-11-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councellor', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('councellorid', models.IntegerField(blank=True, null=True)),
                ('review', models.CharField(blank=True, max_length=30, null=True)),
                ('rating', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
