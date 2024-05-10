from random import randint

from django.db import models
from shop.models import Weapon


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hp = models.IntegerField(default=50)
    money = models.IntegerField(default=100)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('app.User', on_delete=models.CASCADE, null=True)

    # Body
    head = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True, blank=True, related_name="head")
    hands = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True, blank=True, related_name="hands")
    legs = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True, blank=True, related_name="legs")
    armor = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True, blank=True, related_name="armor")

    def __str__(self):
        return f"{self.name} ({self.score})"

    def attack(self):
        attack_total = 0

        if self.hands:
            attack_total += self.hands.attack

        return attack_total

    def defense(self):
        defense_total = 0

        if self.head:
            defense_total += self.head.defense
        if self.legs:
            defense_total += self.legs.defense
        if self.armor:
            defense_total += self.armor.defense

        return defense_total

    def has_weapon(self, weapon):
        return weapon == self.head or \
               weapon == self.hands or \
               weapon == self.legs or \
               weapon == self.armor

    def has_no_money_to_buy(self, weapon):
        return self.money < weapon.money_cost

    def weapon_transaction(self, weapon, is_buying):
        w = weapon if is_buying else None

        if weapon.type == 'HEAD':
            self.head = w
        elif weapon.type == 'HAND':
            self.hands = w
        elif weapon.type == 'LEGS':
            self.legs = w
        elif weapon.type == 'ARMOR':
            self.armor = w


class Enemy(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hp = models.IntegerField(default=5)
    money_drop = models.IntegerField(default=0)
    attack = models.IntegerField()
    defense = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "enemies"

    def __str__(self):
        return f"{self.name} | Drop: ${self.money_drop} | HP: {self.hp}"

    def atq_variation(self):
        min_atq = int(self.attack * 0.25)
        return randint(min_atq, self.attack)

    def money_variation(self):
        min_money = int(self.money_drop * 0.50)
        return randint(min_money, self.money_drop)

    def score_given(self):
        return int(self.atq_variation() * 0.25 + self.money_variation() * 0.25 + 1)
