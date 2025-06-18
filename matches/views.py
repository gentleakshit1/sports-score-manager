from django.shortcuts import render, get_object_or_404, redirect
from .models import Match
from scoreboard.models import TeamInning, PlayerPerformance, Player, BallEvent
from scoreboard.utils import update_score
from django.http import HttpResponse
from django.template.loader import render_to_string

def match_scoreboard(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    innings = TeamInning.objects.filter(match=match)
    players_stats = PlayerPerformance.objects.filter(match=match).select_related('player', 'player__team')

    html = render_to_string('matches/components/scoreboard_content.html', {
        'match': match,
        'innings': innings,
        'players_stats': players_stats,
    })
    return HttpResponse(html)



def match_list(request):
    matches = Match.objects.filter(status__in=["upcoming", "live"]).order_by('start_time')
    return render(request, 'matches/list.html', {'matches': matches})


def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    innings = TeamInning.objects.filter(match=match)
    players_stats = PlayerPerformance.objects.filter(match=match).select_related('player', 'player__team')

    # Add overs_bowled_display to each player
    for p in players_stats:
        overs = p.balls_bowled // 6
        balls = p.balls_bowled % 6
        p.overs_bowled_display = f"{overs}.{balls}" if p.balls_bowled > 0 else "0.0"

    return render(request, 'matches/detail.html', {
        'match': match,
        'innings': innings,
        'players_stats': players_stats,
    })

from django.contrib.auth.decorators import login_required, user_passes_test

def is_scorekeeper(user):
    return user.groups.filter(name='Scorekeepers').exists() or user.is_superuser

@login_required
@user_passes_test(is_scorekeeper)
def live_score_panel(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    players = Player.objects.filter(team__in=[match.team1, match.team2])

    if request.method == 'POST':
        batsman_id = request.POST['batsman']
        bowler_id = request.POST['bowler']
        runs = int(request.POST.get('runs', 0))
        ball_type = request.POST.get('ball_type', 'normal')
        is_wicket = 'wicket' in request.POST

        # ✅ Create BallEvent
        BallEvent.objects.create(
            match=match,
            batsman_id=batsman_id,
            bowler_id=bowler_id,
            runs=runs,
            ball_type=ball_type,
            is_wicket=is_wicket
        )

        # ✅ Update scoreboard
        update_score(
            match=match,
            batsman=Player.objects.get(id=batsman_id),
            bowler=Player.objects.get(id=bowler_id),
            runs=runs,
            ball_type=ball_type,
            is_wicket=is_wicket
        )

        return redirect('live_score_panel', match_id=match_id)

    return render(request, 'matches/live_score_panel.html', {
        'match': match,
        'players': players,
    })
