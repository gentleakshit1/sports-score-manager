from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeamRegistrationForm, PlayerForm
from .models import Team, Player
from django.forms import modelformset_factory

def team_register_basic(request):
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team_add_players', team_id=team.id)
    else:
        form = TeamRegistrationForm()
    
    return render(request, 'teams/register_team.html', {'form': form})

def team_add_players(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=11)

    if request.method == 'POST':
        formset = PlayerFormSet(request.POST, queryset=Player.objects.none())
        if formset.is_valid():
            for form in formset:
                player = form.save(commit=False)
                player.team = team
                player.save()
            return redirect('registration_success')  # or scoreboard
    else:
        formset = PlayerFormSet(queryset=Player.objects.none())

    return render(request, 'teams/add_players.html', {
        'team': team,
        'formset': formset
    })
def registration_success(request):
    return render(request, 'teams/registration_success.html')
