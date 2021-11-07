from django.db import models
from django.utils import timezone


class Task(models.Model):
    task_title = models.CharField('Имя задачи', max_length=100)
    task_text = models.TextField('Содержание', max_length=200)
    pub_date = models.DateTimeField('Дата создания', default=timezone.now)
    task_date = models.DateTimeField('Дата задачи')
    start_time = models.TimeField('Начало')
    end_time = models.TimeField('Окончание')

    def __str__(self):
        return self.task_title

    @property
    def is_actual(self):
        return self.task_date >= timezone.now()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
