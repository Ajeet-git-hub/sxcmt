# Generated by Django 4.2.3 on 2023-08-02 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_book_as_rt_issue_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book_as_rt',
        ),
    ]
