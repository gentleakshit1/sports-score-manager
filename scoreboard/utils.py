from .models import PlayerPerformance, TeamInning
from matches.models import Match
from teams.models import Player

def update_score(match, batsman, bowler, runs, ball_type, is_wicket):
    # ✅ Update TeamInning
    inning, _ = TeamInning.objects.get_or_create(match=match, team=batsman.team)

    inning.runs += runs
    if is_wicket:
        inning.wickets += 1
    if ball_type == 'normal':
        inning.overs_played += (1 / 6)  # update this to a smarter counter later
    inning.save()

    # ✅ Update Batsman Performance
    batsman_perf, _ = PlayerPerformance.objects.get_or_create(match=match, player=batsman)
    if ball_type == 'normal':
        batsman_perf.balls_faced += 1
    batsman_perf.runs_scored += runs
    if runs == 4:
        batsman_perf.fours += 1
    if runs == 6:
        batsman_perf.sixes += 1
    batsman_perf.save()

    # ✅ Update Bowler Performance
    bowler_perf, _ = PlayerPerformance.objects.get_or_create(match=match, player=bowler)
    if ball_type == 'normal':
        bowler_perf.balls_bowled += 1
    bowler_perf.runs_conceded += runs
    if is_wicket:
        bowler_perf.wickets_taken += 1
    bowler_perf.save()
