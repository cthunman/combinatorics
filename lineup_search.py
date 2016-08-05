import csv, copy, sys
from decimal import *

def read_salary_data(csv_file):
	with open(csv_file) as csvfile:
		salary_list = []
		reader = csv.DictReader(csvfile)
		for row in reader:
			positions = row['Position'].split('/')

			row['PPD'] = Decimal(row['AvgPointsPerGame']) / Decimal(row['Salary'])
			for p in positions:
				r = copy.copy(row)
				r['Position'] = p
				salary_list.append(r)

	return salary_list

def sort_by(salary_list, key):
	sorted_salaries = {}
	for s in salary_list:
		if s[key] not in sorted_salaries:
			sorted_salaries[s[key]] = []
		sorted_salaries[s[key]].append(s)

	for key in sorted_salaries:
		# sorted_salaries[key] = sorted(sorted_salaries[key], key=lambda x : x['PPD'], reverse=True)
		sorted_salaries[key] = sorted(sorted_salaries[key], 
			key=lambda x : x['AvgPointsPerGame'], 
			reverse=True
		)

	return sorted_salaries

def find_worst_ppg(lineup):
	sorted_lineup = sorted(lineup, key=lambda x : x['PPD'], reverse=True)
	return sorted_lineup[0]

def scan_lineups(sorted_salaries, num_lineups, selections):

	index_map = {}
	for s in selections:
		index_map[s] = 0

	current_lineup = []
	for s in selections:
		for i in range(selections[s]):
			current_lineup.append(sorted_salaries[s][index_map[s]])
			index_map[s] = index_map[s] + 1

	salary_total = 0
	for p in current_lineup:
		salary_total = salary_total + int(p['Salary'])
	# while salary_total > 50000:
	lineup_count = 0
	while lineup_count < num_lineups:
		worst_player = find_worst_ppg(current_lineup)
		current_lineup.remove(worst_player)
		current_lineup.append(sorted_salaries[worst_player['Position']][index_map[worst_player['Position']]])
		index_map[worst_player['Position']] = index_map[worst_player['Position']] + 1
		salary_total = 0
		points_total = 0
		for p in current_lineup:
			salary_total = salary_total + int(p['Salary'])
			points_total = points_total + Decimal(p['AvgPointsPerGame'])
		if salary_total < 50000:
			print '-------------'
			print current_lineup
			print 'salary_total ' + unicode(salary_total)
			print 'points_total ' + unicode(points_total)

			print '-------------'
			lineup_count = lineup_count + 1

	
	# for i in range(num_lineups):
	# 	current_lineup = []
		# for s in selections:


def main():
	sport = sys.argv[1]
	print sport

	if sport == 'baseball':
		filename = 'data/Baseball20160802.csv'
		selections = {
			'SP' : 2,
			'C' : 1,
			'1B' : 1,
			'2B' : 1,
			'3B' : 1,
			'SS' : 1,
			'OF' : 3,
		}
	elif sport == 'golf':
		filename = 'data/Golf20160804.csv'
		selections = {
			'G' : 6
		}

	salary_list = read_salary_data(filename)

	sorted_salaries = sort_by(salary_list, 'Position')
	for s in sorted_salaries:
		print s
	# for s in sorted_salaries:
	# 	print '-----------------'
	# 	print s
	# 	for r in sorted_salaries[s]:
	# 		print r
	
	
	scan_lineups(sorted_salaries, 5, selections)

if __name__ == '__main__':
	main()
