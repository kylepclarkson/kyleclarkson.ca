# Generated by Django 3.1.2 on 2021-01-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_auto_20210129_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateField(blank=True),
        ),
    ]