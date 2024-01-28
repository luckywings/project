# Generated by Django 5.0 on 2023-12-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('decription', models.TextField(max_length=500)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
