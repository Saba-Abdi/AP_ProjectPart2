# Generated by Django 4.0 on 2024-01-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='cost',
            field=models.IntegerField(),
        ),
    ]