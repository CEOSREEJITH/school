from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=250)
    dob=models.TextField()
    age = models.TextField()
    gender= models.TextField()
    mailid = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    materials = models.TextField()

    def __str__(self):
        return self.name