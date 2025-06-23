from django import forms
from .models import Match, Team

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'overs_limit', 'venue', 'start_time','toss_winner']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add an empty label to toss_winner field
        self.fields['toss_winner'].queryset = Team.objects.all()
        self.fields['toss_winner'].empty_label = "Coin not tossed yet"