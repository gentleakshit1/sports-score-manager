from django.db import models
from matches.models import Match
from teams.models import Team, Player

class TeamInning(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs_played = models.FloatField(default=0.0)  # e.g., 18.3 overs → 18.5

    def __str__(self):
        return f"{self.team.name} - {self.runs}/{self.wickets} in {self.overs_played} overs"


class PlayerPerformance(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    # Batting stats
    runs_scored = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)

    # Bowling stats
    balls_bowled = models.IntegerField(default=0)
    runs_conceded = models.IntegerField(default=0)
    wickets_taken = models.IntegerField(default=0)

    def strike_rate(self):
        return (self.runs_scored / self.balls_faced * 100) if self.balls_faced > 0 else 0

    def economy_rate(self):
        overs = self.balls_bowled / 6
        return (self.runs_conceded / overs) if overs > 0 else 0

    def __str__(self):
        return f"{self.player.name} in {self.match}"

class BallEvent(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    batsman = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name="batting_events")
    bowler = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name="bowling_events")
    runs = models.IntegerField(default=0)
    is_wicket = models.BooleanField(default=False)

    BALL_TYPE_CHOICES = [
        ('normal', 'Normal'),
        ('wide', 'Wide'),
        ('no_ball', 'No Ball'),
        ('bye', 'Bye'),
        ('leg_bye', 'Leg Bye'),
    ]
    ball_type = models.CharField(max_length=20, choices=BALL_TYPE_CHOICES, default='normal')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.match} - {self.batsman} vs {self.bowler} ({self.runs} runs)"
