# Generated by Django 4.0.5 on 2022-06-16 10:39

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_localevent_remove_eventindex_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventindex',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
