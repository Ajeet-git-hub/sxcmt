# Generated by Django 4.2.3 on 2023-08-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_remove_book_book_quantity_book_book_left_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_left',
        ),
        migrations.AddField(
            model_name='book',
            name='book_assigned',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
