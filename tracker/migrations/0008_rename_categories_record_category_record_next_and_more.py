# Generated by Django 5.0.6 on 2024-08-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_record_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='categories',
            new_name='category',
        ),
        migrations.AddField(
            model_name='record',
            name='next',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='record',
            name='prev',
            field=models.BooleanField(default=False),
        ),
    ]
