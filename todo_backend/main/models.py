from django.db import models

class ToDoTask(models.Model):
    title = models.CharField('Task Name', max_length=100, default='')
    description = models.CharField('Description of task', max_length=255, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


