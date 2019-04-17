from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

MACULATURA = 'mc'
IRON = 'ir'
PLASTIC = 'pl'
GLASS = 'gl'

TRASH_CHOICES = (
    (MACULATURA, 'Макулатура'),
    (IRON, 'Железо'),
    (PLASTIC, 'Пластик'),
    (GLASS, 'Стекло'),
)
# Create your models here.


class Trash(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trash')
    trash_type = models.CharField(
        max_length=2, choices=TRASH_CHOICES, default=None)
    weight = models.PositiveIntegerField()

    def __str__(self):
        return self.trash_type
