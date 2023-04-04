from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    money_cost = models.IntegerField()
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    type = models.CharField(
        max_length=5,
        choices=[
            ('HEAD', 'Casco'),
            ('HAND', 'Una Mano'),
            ('LEGS', 'Piernas'),
            ('ARMOR', 'Armadura'),
        ],
        default=None
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.name} (${self.money_cost}) | atq: {self.attack} | def: {self.defense}"

    def cost_for_selling(self):
        return int(self.money_cost / 2)
