# Generated by Django 3.0.2 on 2020-01-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0005_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('original_img', models.ImageField(upload_to='original/')),
                ('compress_img', models.ImageField(upload_to='compress/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
