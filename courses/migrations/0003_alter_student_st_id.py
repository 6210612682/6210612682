# Generated by Django 3.2.7 on 2021-09-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_id',
            field=models.CharField(max_length=10),
        ),
    ]
