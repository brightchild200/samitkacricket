from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('All-rounder', 'All-rounder')])
    runs = models.IntegerField(default=0)
    batting_avg = models.FloatField(default=0.0)
    fifties = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    bowling_avg = models.FloatField(default=0.0)
    economy = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Match(models.Model):
    date = models.DateField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()
    opponent = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.player.name} vs {self.opponent} on {self.date}"