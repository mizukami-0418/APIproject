from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username