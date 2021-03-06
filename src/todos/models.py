from django.db import models

from app.models import DefaultModel


class Todo(DefaultModel):
    text = models.TextField()
    assignee = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=255, default='opened')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.text
