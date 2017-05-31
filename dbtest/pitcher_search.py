import mlbgame
import datetime

for i in range(10):
    day = datetime.date.today() - datetime.timedelta(i)
    print day
    print mlbgame.day(day.year, day.month, day.day)

games = mlbgame.day(2016, 8, 2)
stats = mlbgame.player_stats(games[4].game_id)

print '\nHOME PITCHING\n'
for s in stats['home_pitching']:
    print s

print '\nHOME BATTING\n'
for s in stats['home_batting']:
    print s

print '\nAWAY PITCHING\n'
for s in stats['away_pitching']:
    print s

print '\nAWAY BATTING\n'
for s in stats['away_batting']:
    print s

print '-------'


# print stats.__dict__
print dir(stats)

points_by_opponent = {}
