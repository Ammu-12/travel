from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
def __str__(self):
    return self.name
class team(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    contact=models.IntegerField()

def __str__(self):
        return self.name