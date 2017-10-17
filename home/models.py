from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=250)

    description = models.TextField()

    image = models.ImageField(upload_to='home/media/')

    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Apps"

        verbose_name_plural = "Apps"