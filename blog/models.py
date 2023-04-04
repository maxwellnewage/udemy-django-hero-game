from django.db import models

from app.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=[
            ('PA', 'Parches'),
            ('ME', 'Mejoras'),
            ('EV', 'Eventos')
        ],
        default=None
    )
    title = models.CharField(max_length=50)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.title} | {self.category} | @{self.author}"
