from django import forms
from .models import Team, Player, Department

class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'department']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'role', 'batting_style', 'bowling_style', 'jersey_number']
