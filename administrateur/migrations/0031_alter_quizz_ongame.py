# Generated by Django 4.1.7 on 2023-05-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0030_alter_quizz_ongame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='onGame',
            field=models.IntegerField(default=0),
        ),
    ]