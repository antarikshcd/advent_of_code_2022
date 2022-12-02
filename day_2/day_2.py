"""
Day 2 of advent of code 2022

"""
def game(opponent, player):
    """
    """
    points_dict = {'rock': 1, 'paper': 2, 'scissor': 3}
    outcome_dict = {'X': 'rock', 'Y': 'paper', 'Z': 'scissor'}
    game_dict = {'rock' : {'A' : 3,
                           'B' : 0,
                           'C' : 6},
                 'paper' : {'A' : 6,
                            'B' : 3,
                            'C' : 0},                          
                 'scissor' : {'A' : 0,
                              'B' : 6,
                              'C' : 3},
    }
    #
    play = outcome_dict[player]
    score = points_dict[play] + game_dict[play][opponent]

    return score

def game_revamped(opponent, player):
    """
    """
    # player_dict = {'X': 1, 'Y': 2, 'Z': 3}
    points_dict = {'rock': 1, 'paper': 2, 'scissor': 3}
    match_dict = {'win': 6, 'draw': 3, 'lose': 0}
    outcome_dict = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    #
    game_dict = {'win' : {'A' : 'paper',
                          'B' : 'scissor',
                          'C' : 'rock'},
                 'lose' : {'A' : 'scissor',
                           'B' : 'rock',
                           'C' : 'paper'},                          
                 'draw' : {'A' : 'rock',
                           'B' : 'paper',
                           'C' : 'scissor'},
    }
    #
    outcome = outcome_dict[player]
    # when player is winner
    play = game_dict[outcome][opponent]
    score = points_dict[play] + match_dict[outcome]
    # score = player_dict[player] + match_dict[outcome]


    return score    

points_dict = {'X': 1, 'Y': 2, 'Z': 3}
#
opponent_list = []
player_list = []
#
with open('./input.txt', 'r') as file:
    #
    for line in file:
        txt = line.strip()
        txt_split = txt.split()
        opponent_list.append(txt_split[0])
        player_list.append(txt_split[1])
        # print(txt_split)

# map
score_list = map(game, opponent_list, player_list)
total_score = sum(score_list)
#
#print(list(score_list)) 
print(f'Total score part 1: {total_score}') 
#
score_revamped = map(game_revamped, opponent_list, player_list)       
print(f'Total score part 2: {sum(score_revamped)}')