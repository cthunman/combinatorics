import nflgame

print 'FOOTBALL'
games = nflgame.games(2015, week=2)
# players = nflgame.combine_game_stats(games)
# for p in players.rushing().sort('rushing_yds').limit(5):
# 	msg = '%s %d carries for %d yards and %d TDs'
# 	print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)

# print '\n\n\n\n'
# for p in players.rushing().sort('rushing_yds').limit(5):
# 	print p



# for g in games:
g = games[0]
print g
# print '\n'
# print dir(g)
# print '\n'
# print g.players
stat_dict = {}
for p in g.players:
	# print dir(p)
	stat_dict[p] = {}
	for s in p.formatted_stats().split(','):
		tokens = s.split(':')
		stat_dict[p][tokens[0]] = int(tokens[1])

# print stat_dict
for p in stat_dict:
	print p, stat_dict[p]
	print '\n'

# print '\n'
# print g.home
# print g.away

	# print 'g.home_team'
	# print g.home_team
	# print 'g.away_team'
	# print g.away_team
