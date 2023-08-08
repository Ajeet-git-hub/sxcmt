# Generated by Django 4.2.3 on 2023-08-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=40)),
                ('student_roll', models.CharField(max_length=20)),
                ('book', models.ManyToManyField(to='library.book')),
            ],
        ),
    ]
