from django import forms
from .models import CustomUser

GAME_CHOICES = [
    ('football', 'Football'),
    ('basketball', 'Basketball'),
    ('cricket', 'Cricket'),
]

class CompleteProfileForm(forms.ModelForm):
    forms.ChoiceField(
        choices=GAME_CHOICES,
        widget=forms.Select, 
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ['full_name', 'role', 'department', 'year_of_study', 'gender', 'games']
        widgets = {
            'gender': forms.Select(choices=CustomUser._meta.get_field('gender').choices),
            'role': forms.Select(choices=CustomUser._meta.get_field('role').choices),
            'games': forms.Select(choices=CustomUser._meta.get_field('games').choices),
        }

    def clean_games(self):
        return self.cleaned_data['games']  # returns list (perfect for JSONField)
