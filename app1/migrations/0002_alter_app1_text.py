# Generated by Django 5.0.6 on 2024-07-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app1',
            name='text',
            field=models.CharField(max_length=240),
        ),
    ]
