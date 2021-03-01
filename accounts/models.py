from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    # ligaçao um para um, usada para extençoes
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # AUTH_USER_MODEL - cria campos de preenchimento (first, last name, email, password)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    # bio = models.TextField()

    def __str__(self):
        return f'Profile for user {self.user.username}'