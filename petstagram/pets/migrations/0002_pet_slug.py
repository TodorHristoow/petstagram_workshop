# Generated by Django 4.2.3 on 2023-07-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]