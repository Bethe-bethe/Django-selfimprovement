# Generated by Django 4.0.4 on 2023-02-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0044_remove_books_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
