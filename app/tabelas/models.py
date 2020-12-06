from django.db import models
from django.contrib.auth.models import AbstractUser as GenericUser


class User(GenericUser):
    profile_pic = models.ImageField(upload_to='media/images', blank=True, null=True)
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Publicacao(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='media/images')
    criado_em = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    publicacao = models.ForeignKey('Publicacao', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    deslike = models.BooleanField(default=False)


class Comentario(models.Model):
    publicacao = models.ForeignKey('Publicacao', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comentario = models.TextField()



