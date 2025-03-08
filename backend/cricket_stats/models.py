from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()
    batting_average = models.FloatField()
    bowling_average = models.FloatField()

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