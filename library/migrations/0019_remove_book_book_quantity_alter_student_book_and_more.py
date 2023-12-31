# Generated by Django 4.2.3 on 2023-08-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_quantity',
        ),
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.ManyToManyField(blank=True, to='library.book'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_roll',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
