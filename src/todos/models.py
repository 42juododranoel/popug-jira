from django.db import models

from app.models import DefaultModel


class Todo(DefaultModel):
    text = models.CharField(max_length=255)
    assignee = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.text
