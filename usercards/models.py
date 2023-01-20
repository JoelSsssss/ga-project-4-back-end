from django.db import models


class UserCards(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    template = models.ManyToManyField(
        'templates.Templates', related_name="usercards")

    def __str__(self):
        return f"{self.name} - {self.author}"
