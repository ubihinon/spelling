from django.core.validators import FileExtensionValidator
from django.db import models


class Card(models.Model):
    text = models.CharField(max_length=200)
    sound = models.FileField(
        upload_to='sounds/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp3'])
        ]
    )

    class Meta:
        ordering = ('text',)

    def __str__(self):
        return self.text
