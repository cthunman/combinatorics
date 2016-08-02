import mlbgame
import nflgame
games = mlbgame.day(2016, 8, 1)
print 'BASEBALL'
for game in games:
	print game

print 'FOOTBALL'
games = nflgame.games(2015, week=6)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(5):
	msg = '%s %d carries for %d yards and %d TDs'
	print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)