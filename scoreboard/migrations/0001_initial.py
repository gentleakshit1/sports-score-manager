# Generated by Django 5.2.3 on 2025-06-17 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs_scored', models.IntegerField(default=0)),
                ('balls_faced', models.IntegerField(default=0)),
                ('fours', models.IntegerField(default=0)),
                ('sixes', models.IntegerField(default=0)),
                ('balls_bowled', models.IntegerField(default=0)),
                ('runs_conceded', models.IntegerField(default=0)),
                ('wickets_taken', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.player')),
            ],
        ),
        migrations.CreateModel(
            name='TeamInning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('overs_played', models.FloatField(default=0.0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
