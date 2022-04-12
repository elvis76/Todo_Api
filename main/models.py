from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Todo(models.Model):
    task = models.CharField(max_length=300)
    desc = models.TextField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20,
                              default="pending", 
                              choices=[
                                  ("pending", "Pending"),
                                   ("completed", "Completed")
                                  ])
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             related_name="tasks")
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.task} for {self.user.id}'