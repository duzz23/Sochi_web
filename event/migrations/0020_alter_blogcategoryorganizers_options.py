# Generated by Django 4.0.5 on 2022-07-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_alter_blogcategoryorganizers_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategoryorganizers',
            options={'ordering': ['name'], 'verbose_name': 'Организатор и  Контрибьютор', 'verbose_name_plural': 'Организаторы и  Контрибьюторы'},
        ),
    ]