from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from character.models import Player
from shop.models import Weapon


@login_required(login_url='login')
def shop(request):
    player = Player.objects.filter(owner=request.user).first()
    weapons = Weapon.objects.all()

    for weapon in weapons:
        weapon.is_equipped = player.has_weapon(weapon)

    return render(request, 'shop.html', {
        'weapons': weapons,
        'player': player
    })


@login_required(login_url='login')
def buy(request, weapon_id):
    player = Player.objects.filter(owner=request.user).first()
    weapon = Weapon.objects.get(id=weapon_id)

    if player.has_no_money_to_buy(weapon):
        messages.error(request, 'No puedes permitirte esto!')
        return redirect('shop')

    player.money -= weapon.money_cost
    player.weapon_transaction(weapon, True)
    player.save()

    return redirect('shop')


@login_required(login_url='login')
def sell(request, weapon_id):
    player = Player.objects.filter(owner=request.user).first()
    weapon = Weapon.objects.get(id=weapon_id)

    player.money += weapon.cost_for_selling()
    player.weapon_transaction(weapon, False)
    player.save()

    return redirect('shop')
