from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def validate_difficulty(value):
    if value > 4 or value < 1:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

# Create your models here.
class Todolist(models.Model):
    list_name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.list_name


class Todo(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    difficulty = models.IntegerField(validators=[validate_difficulty])
    is_complete = models.BooleanField(default=False)
    todolist = models.ForeignKey(Todolist,related_name= "todo_set", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

