# Generated by Django 3.1.2 on 2021-01-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0012_remove_article_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_published',
            field=models.DateField(auto_now=True),
        ),
    ]
