# Generated by Django 3.2.5 on 2021-08-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0002_alter_movies_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.CharField(default='No Title', max_length=50, unique=True),
        ),
    ]
