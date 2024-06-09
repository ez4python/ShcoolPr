from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.phone}'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images')
    descriptions = models.TextField()
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.title}"

