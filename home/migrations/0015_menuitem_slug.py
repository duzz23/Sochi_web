# Generated by Django 4.0.5 on 2022-07-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_privacypolicy_remove_menuitem_hero_cta_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
