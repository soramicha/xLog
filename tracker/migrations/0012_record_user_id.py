# Generated by Django 5.0.6 on 2024-08-17 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_remove_record_next_remove_record_prev_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
