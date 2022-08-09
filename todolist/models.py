from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    is_complete = models.IntegerField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.todo