import csv, copy
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
		sorted_salaries[key] = sorted(sorted_salaries[key], key=lambda x : x['PPD'], reverse=True)

	return sorted_salaries

def scan_baseball_lineups(sorted_salaries, num_lineups):
	selections = {
		'P' : 2,
		'C' : 1,
		'1B' : 1,
		'2B' : 1,
		'3B' : 1,
		'SS' : 1,
		'OF' : 3,
	}

	index_map = {}
	for s in selections:
		index_map[s] = 0

	current_lineup = []
	for s in selections:
		for i in range(selections[s]):
			index_map[s] = index_map[s] + 1
			

	for i in range(num_lineups):
		current_lineup = []
		# for s in selections:


def main():
	salary_list = read_salary_data('data/DKSalariesBaseball.csv')

	sorted_salaries = sort_by(salary_list, 'Position')
	for s in sorted_salaries:
		print '-----------------'
		print s
		for r in sorted_salaries[s]:
			print r

if __name__ == '__main__':
	main()
