from django.db import models

# Create your models here.
class List(models.Model):
    nama = models.CharField(max_length=200)
    alamat = models.TextField()
    email = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)