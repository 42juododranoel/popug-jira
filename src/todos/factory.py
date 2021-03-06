from app.testing import register


@register
def todo(self, **kwargs):
    return self.mixer.blend('todos.Todo', **kwargs)
