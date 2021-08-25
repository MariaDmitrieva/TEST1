# Generated by Django 3.2.6 on 2021-08-25 11:37

import django.core.validators
from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='post_images', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='posts', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]