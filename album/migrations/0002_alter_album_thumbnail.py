# Generated by Django 3.2 on 2021-05-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]
