# Generated by Django 3.1.2 on 2021-01-29 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_auto_20210129_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_published',
        ),
    ]