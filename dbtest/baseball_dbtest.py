import mlbgame

games = mlbgame.day(2016, 8, 2)
print 'BASEBALL'
print '-------'
print unicode(games[4])

stats = mlbgame.player_stats(games[4].game_id)
# print stats.__dict__
print '\nHOME PITCHING\n'
for s in stats['home_pitching']:
	print s

print '\nHOME BATTING\n'
for s in stats['home_batting']:
	print s

print '\AWAY PITCHING\n'
for s in stats['away_pitching']:
	print s

print '\AWAY BATTING\n'
for s in stats['away_batting']:
	print s

print '-------'

# for game in games:
# 	print '-------'
# 	print unicode(game)

# 	stats = mlbgame.player_stats(game.game_id)
# 	# print stats.__dict__
# 	print '\nHOME PITCHING\n'
# 	for s in stats['home_pitching']:
# 		print s

# 	print '\nHOME BATTING\n'
# 	for s in stats['home_batting']:
# 		print s

# 	print '-------'
	# for player in mlbgame.player_stats(game.game_id):
		# print player
	# print type(game)
	# print game.game_id
	# print game.__dict__
