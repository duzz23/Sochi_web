# Generated by Django 4.0.5 on 2022-06-21 14:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='stream',
            field=wagtail.fields.StreamField([('carousel', wagtail.blocks.StructBlock([]))], null=True, use_json_field=False),
        ),
    ]
