from django.contrib import admin
from django.urls import path, include
from matches.views import match_list, match_detail, match_scoreboard
from participants.views import team_register_basic, team_add_players, registration_success
from . import views
from .views import run_migrate, custom_login_redirect
from accounts.views import view_profile
from django.shortcuts import redirect
from accounts.views import profile_check, complete_profile

# 👇 Optional: redirect local login path to Google login
def login_redirect_to_google(request):
    return redirect('/accounts/google/login/')

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🏏 Match listing and details
    path('', match_list, name='match_list'),
    path('match/<int:match_id>/', match_detail, name='match_detail'),
    path('match/<int:match_id>/scoreboard/', match_detail, name='match_scoreboard_full'),
    path('match/<int:match_id>/scoreboard/live/', match_scoreboard, name='match_scoreboard_partial'),

    # 📝 Team registration
    path('register/', team_register_basic, name='team_register'),
    path('register/<int:team_id>/players/', team_add_players, name='team_add_players'),
    path('register/success/', registration_success, name='registration_success'),

    # 📬 Contact & misc
    path('contact/', include('contact.urls')),
    path('developer/', views.developer_view, name='developer'),
    path('run-migrate/', run_migrate),

    # 🔐 Auth / login
    path('login/', custom_login_redirect),  # Your own handler
    path('accounts/login/', login_redirect_to_google),  # Optional override
    path('accounts/', include('allauth.urls')),  # Allauth handles login, logout, etc.
    path('profile-check/', profile_check, name='profile-check'),
    path('complete_profile/', complete_profile, name='complete_profile'),
    path('profile/', view_profile, name='view_profile'),
]
