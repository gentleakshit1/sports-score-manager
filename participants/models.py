from django.db import models

# University departments (like CSE, ECE)
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# A team that plays in the tournament
class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.department.name})"


# A player that belongs to a team
class Player(models.Model):
    ROLE_CHOICES = [
        ('batsman', 'Batsman'),
        ('bowler', 'Bowler'),
        ('allrounder', 'All-Rounder'),
        ('wicketkeeper', 'Wicket-Keeper'),
    ]

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    batting_style = models.CharField(max_length=50, blank=True, null=True)  # Right-hand, Left-hand
    bowling_style = models.CharField(max_length=50, blank=True, null=True)  # Off-spin, Fast
    jersey_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.team.name})"
