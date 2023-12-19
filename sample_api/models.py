from django.db import models

class person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


