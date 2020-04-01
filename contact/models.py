from django.db import models

# Create your models here.
class Contact(models.Model):
    First_Name = models.CharField(max_length = 30)
    Last_Name = models.CharField(max_length = 30)
    Email = models.EmailField(max_length = 100)
    Phone = models.CharField(max_length = 13)
    Subject = models.CharField(max_length = 100)
    Message = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Subject
