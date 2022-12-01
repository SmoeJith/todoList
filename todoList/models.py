from django.db import models

class Todo(models.Model):
    task_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "\"{0}\" ".format(self.task_name) + "created @ {0}, ".format(self.created_at) + "edited @ {0}".format(self.edited_at)