# Generated by Django 4.1.7 on 2023-03-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0014_alter_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizz',
            name='questions',
            field=models.TextField(default=''),
        ),
    ]