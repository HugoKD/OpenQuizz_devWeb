# Generated by Django 4.1.7 on 2023-03-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0009_quizz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizz',
            name='questions',
        ),
        migrations.AddField(
            model_name='quizz',
            name='name',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
