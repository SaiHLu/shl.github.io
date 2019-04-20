from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=225)
    finish = models.BooleanField(default=False)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    def pretty_date(self):
        return self.date.strftime('%b %e %Y')
