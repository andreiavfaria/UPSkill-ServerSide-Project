from django.db import models

# Create your models here.


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)
    pic = models.ImageField(upload_to="director/%Y/%m/%d/", blank=True)
    bio = models.TextField(blank=True)


    def __str__(self):
        return self.name

    class Meta:
        pass
