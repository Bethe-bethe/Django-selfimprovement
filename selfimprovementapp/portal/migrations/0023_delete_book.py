# Generated by Django 4.0.5 on 2022-12-08 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_rename_title_book_bname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
