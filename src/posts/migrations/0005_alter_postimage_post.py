# Generated by Django 3.2.6 on 2021-08-25 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210825_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='posts.post'),
        ),
    ]
