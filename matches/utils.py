from django.core.mail import send_mail
from participants.models import Player

def send_fixture_email(match):
    players_team1 = Player.objects.filter(team=match.team1)
    players_team2 = Player.objects.filter(team=match.team2)
    all_players = list(players_team1) + list(players_team2)
    recipient_list = [p.email for p in all_players if p.email]

    if not recipient_list:
        return  # No emails to send

    subject = f"Fixture: {match.team1.name} vs {match.team2.name}"
    message = f"""
    Dear Player,

    Here are the details for your upcoming match:

    Teams: {match.team1.name} vs {match.team2.name}
    Date & Time: {match.start_time.strftime('%Y-%m-%d %H:%M')}
    Venue: {match.venue}

    Good luck!
    """
    send_mail(subject, message, 'your_email@example.com', recipient_list)
