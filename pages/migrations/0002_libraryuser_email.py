# Generated by Django 5.0.4 on 2024-05-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]