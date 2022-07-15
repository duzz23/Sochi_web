# Generated by Django 4.0.5 on 2022-07-07 08:31

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_alter_blogcategoryorganizers_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategoryorganizers',
            name='slag',
            field=models.SlugField(allow_unicode=True, help_text='Выбрать категорию для Организатора', null=True, verbose_name='slag'),
        ),
        migrations.AlterField(
            model_name='organizers',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='orgs', to='event.blogcategoryorganizers'),
        ),
    ]