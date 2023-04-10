from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from character.models import Player, Enemy


@login_required(login_url='login')
def home(request):
    player = Player.objects.filter(owner=request.user).first()
    enemies = Enemy.objects.all()

    return render(request, 'arena.html', {
        'player': player,
        'enemies': enemies
    })


def attack_enemy(request, enemy_id):
    player = Player.objects.filter(owner=request.user).first()
    enemy = Enemy.objects.get(id=enemy_id)

    battle_result = start_battle(player, enemy)

    return render(request, 'battle.html', {
        'battle': battle_result
    })


def start_battle(player, enemy):
    turn = 'player'
    player_wins = False
    total_player_hp = player.hp
    total_player_damage = 0
    total_enemy_damage = 0

    while player.hp > 0 and enemy.hp > 0:
        if turn == 'player':
            damage = max(player.attack() - enemy.defense, 1)
            enemy.hp -= damage
            total_player_damage += damage
            turn = 'enemy'
        else:
            damage = max(enemy.atq_variation() - player.defense(), 1)
            player.hp -= damage
            total_enemy_damage += damage
            turn = 'player'

    score = money = 0

    if player.hp > 0:
        score = enemy.score_given()
        money = enemy.money_variation()
        player.score += score
        player.money += money
        player_wins = True

    player.hp = total_player_hp
    player.save()

    return {
        'player_damage': total_player_damage,
        'enemy_damage': total_enemy_damage,
        'player_wins': player_wins,
        'score': score,
        'money': money
    }
