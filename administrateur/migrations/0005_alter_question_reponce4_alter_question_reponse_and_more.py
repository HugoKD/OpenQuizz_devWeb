# Generated by Django 4.1.7 on 2023-03-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0004_rename_user_question_pseudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='reponce4',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='reponse',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='reponse1',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='reponse2',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='reponse3',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='reponseVrai',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
