from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from character.forms import PlayerForm
from character.models import Player


@login_required(login_url='login')
def player_profile(request):
    player = Player.objects.filter(owner=request.user).first()

    return render(request, 'character.html', {
      'player': player
    })


@login_required(login_url='login')
def create_player(request):
    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.owner = request.user
            player.save()
            return redirect('player-profile')

    return render(request, 'create_update_form.html', {
        'form': form,
        'title': 'Crear Jugador',
        'submit_value': 'Empieza la aventura!',
        'button_style': 'is-primary'
    })


@login_required(login_url='login')
def update_player(request, player_id):
    player = Player.objects.get(id=player_id)
    form = PlayerForm(instance=player)

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player-profile')

    return render(request, 'create_update_form.html', {
        'form': form,
        'title': f'Editar {player.name}',
        'submit_value': 'Modifica a tu héroe',
        'button_style': 'is-warning'
    })


@login_required(login_url='login')
def delete_player(request, player_id):
    player = Player.objects.get(id=player_id)

    player.delete()
    return redirect('player-profile')
