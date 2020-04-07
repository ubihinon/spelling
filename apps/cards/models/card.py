from django.db import models


class Card(models.Model):
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ('text',)

    def __str__(self):
        return self.text
