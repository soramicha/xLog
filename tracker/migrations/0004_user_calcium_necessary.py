# Generated by Django 5.0.6 on 2024-07-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_remove_user_pregnancy_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='calcium_necessary',
            field=models.IntegerField(default=0),
        ),
    ]
