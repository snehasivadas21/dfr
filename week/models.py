from django.db import models

class Students(models.Model):
    stu_id=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
