"""
URL configuration for sangathan_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from matches.views import match_list, match_detail, match_scoreboard
from teams.views import team_register_basic, team_add_players, registration_success
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', match_list, name='match_list'),
    path('match/<int:match_id>/', match_detail, name='match_detail'),

    # 🏏 Cricheroes-style registration
    path('register/', team_register_basic, name='team_register'),
    path('register/<int:team_id>/players/', team_add_players, name='team_add_players'),

    #live scoreboard
    path('match/<int:match_id>/scoreboard/', match_detail, name='match_scoreboard_full'),
    path('match/<int:match_id>/scoreboard/live/', match_scoreboard, name='match_scoreboard_partial'),
    path('register/success/', registration_success, name='registration_success'),
    path("contact/", include("contact.urls")),
    path("developer/", views.developer_view, name="developer"),
    

    

    # path('register/', views.team_register_basic, name='team_register'),  # Removed duplicate, already defined above
    # path('register/<int:team_id>/players/', views.team_add_players, name='team_add_players'),  # Removed duplicate
    # path('register/success/', views.registration_success, name='registration_success'),  # Uncomment and import if needed

]

