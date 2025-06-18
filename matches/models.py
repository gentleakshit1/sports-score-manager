from django.db import models
from teams.models import Team

class Match(models.Model):
    MATCH_STATUS = [
        ('upcoming', 'Upcoming'),
        ('live', 'Live'),
        ('completed', 'Completed'),
    ]

    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    overs_limit = models.IntegerField(default=20)  # T20 format by default
    venue = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=MATCH_STATUS, default='upcoming')

    toss_winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='won_toss_matches')
    toss_decision = models.CharField(max_length=10, choices=[('bat', 'Bat'), ('bowl', 'Bowl')], null=True, blank=True)

    result = models.CharField(max_length=255, blank=True, null=True)  # e.g., "CSE Warriors won by 10 runs"

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} @ {self.venue} - {self.get_status_display()}"
