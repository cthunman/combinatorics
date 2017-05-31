import itertools
from player_reader import read_file


# input list of vectors of (list, number to select)
def select_combinations(combo_list):
    # for combo in combo_list:

    combos = []
    for combo in combo_list:
        combos.append(itertools.combinations(combo[0], combo[1]))

    combined_results = itertools.product(*combos)
    result_list = []
    for r in combined_results:
        result_list.append([i for sub in r for i in sub])

    return result_list


def filter(player_list, key, value):
    filter_list = []
    for player in player_list:
        if player[key] == value:
            filter_list.append(player)
    return filter_list


def main():

    player_list = read_file('data/DKSalaries.csv')

    qb_list = filter(player_list, 'Position', 'QB')
    rb_list = filter(player_list, 'Position', 'RB')
    wr_list = filter(player_list, 'Position', 'WR')
    te_list = filter(player_list, 'Position', 'TE')
    dst_list = filter(player_list, 'Position', 'DST')

    # QB, RB1, RB2, WR1, WR2, WR3, TE, FLEX (RB/WR/TE), and DST
    # qb_list = ['Tom Brady QB', 'Ben Roethlisberger QB']
    # rb_list = ['Marshawn Lynch RB',
    # 'Earl Campbell RB',
    # 'LaDainian Tomlinson RB',
    # 'Eric Dickerson RB']
    # wr_list = ['Demaryius Thomas WR',
    # 'Calvin Johnson WR',
    # 'Dez Bryant WR',
    # 'Antonio Brown WR']
    # te_list = ['Rob Gronkowski TE', 'Ryan Griffin TE']
    # dst_list = ['Patriots DST', 'Seahawks DST', 'Redskins DST']

    results = select_combinations([
            (qb_list, 1),
            (rb_list, 2),
            (wr_list, 3),
            (te_list, 1),
            (dst_list, 1),
        ])

    for result in results:
        print result

if __name__ == '__main__':
    main()
