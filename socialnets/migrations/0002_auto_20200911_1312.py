# Generated by Django 2.2.15 on 2020-09-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
