# Generated by Django 3.0 on 2019-12-28 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='media_training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(max_length=1000)),
                ('url_image', models.ImageField(upload_to='')),
                ('pub_create', models.DateTimeField(verbose_name='date de création')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apps')),
            ],
        ),
    ]
