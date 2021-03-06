# Generated by Django 4.0.5 on 2022-06-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('member', '0002_member_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
