import csv

def read_file(filename):

	player_list = []
	with open(filename) as player_file:
		# fieldnames = ["Position","Name","Salary","GameInfo","AvgPointsPerGame","teamAbbrev"]
		reader = csv.DictReader(player_file)

		for row in reader:

			player = {}
			player['Position'] = row['Position']
			player['Name'] = row['Name']
			player['Salary'] = row['Salary']
			player['GameInfo'] = row['GameInfo']
			player['AvgPointsPerGame'] = row['AvgPointsPerGame']
			player['teamAbbrev'] = row['teamAbbrev']

			player_list.append(player)

	return player_list
