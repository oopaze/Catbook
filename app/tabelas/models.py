from django.db import models
from django.contrib.auth.models import AbstractUser as GenericUser

class User(GenericUser):

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
