# Generated by Django 3.0.2 on 2020-01-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0002_auto_20200122_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
