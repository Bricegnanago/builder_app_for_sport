# Generated by Django 3.0 on 2020-01-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_media_training_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media_training',
            name='instruction',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='media_training',
            name='url_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='media_training',
            name='videofile',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]