# Generated by Django 4.1.7 on 2023-04-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0021_question_intitule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.CharField(default='', max_length=255),
        ),
    ]