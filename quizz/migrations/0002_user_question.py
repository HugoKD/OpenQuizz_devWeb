# Generated by Django 4.1.7 on 2023-04-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='question',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]