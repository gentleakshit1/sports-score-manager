from django.contrib import admin
from .models import Match
from .forms import MatchForm  # import your custom form
from .utils import send_fixture_email

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    form = MatchForm  # ✅ connect your form here
    list_display = ('team1', 'team2', 'venue', 'start_time', 'status')
    actions = ['send_fixture_notifications']

    def send_fixture_notifications(self, request, queryset):
        for match in queryset:
            send_fixture_email(match)
        self.message_user(request, "Fixture emails sent to all participants.")
    send_fixture_notifications.short_description = "Send fixture emails to all players"


