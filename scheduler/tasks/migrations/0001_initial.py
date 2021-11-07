# Generated by Django 2.2.24 on 2021-11-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100, verbose_name='Имя задачи')),
                ('task_text', models.TextField(max_length=200, verbose_name='Содержание')),
                ('pub_date', models.DateTimeField(verbose_name='Дата создания')),
                ('task_date', models.DateTimeField(verbose_name='Дата задачи')),
                ('start_time', models.TimeField(verbose_name='Начало')),
                ('end_time', models.TimeField(verbose_name='Окончание')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]