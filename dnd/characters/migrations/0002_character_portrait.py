# Generated by Django 4.2.3 on 2023-08-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='portrait',
            field=models.ImageField(null=True, upload_to='portrait/'),
        ),
    ]