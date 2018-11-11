import numpy as np
import random

balls_in_an_over = 6
runs = (0, 1, 2, 3, 4, 5, 6, -1)
remaining_overs = 4
total_balls = remaining_overs * 6
runs_needed = 40
total_runs_scored = 0

KB_prob = (5, 30, 25, 10, 15, 1, 9, 5)
NS_prob = (10, 40, 20, 5, 10, 1, 4, 10)
RR_prob = (20, 30, 15, 5, 5, 1, 4, 20)
SH_prob = (30, 25, 5, 0, 5, 1, 4, 30)

KB = np.repeat(runs, KB_prob, axis=0)
NS = np.repeat(runs, NS_prob, axis=0)
RR = np.repeat(runs, RR_prob, axis=0)
SH = np.repeat(runs, SH_prob, axis=0)


player_dictionary = {
    'KB': {
        'probability': KB,
        'score': 0,
        'balls': 0,
    },
    'NS': {
        'probability': NS,
        'score': 0,
        'balls': 0,
    },
    'RR': {
        'probability': RR,
        'score': 0,
        'balls': 0,
    },
    'SH': {
        'probability': SH,
        'score': 0,
        'balls': 0,
    }
}

available_batsmen = ['KB', 'NS', 'RR', 'SH']
all_batsmen = ['Kirat Bohli (KB)', 'N.S Nodhi (NS)', 'R Rumrah (RR)', 'Shashi Henra (SH)']
batsmen = available_batsmen[0]

# initial commentary
print('Last', remaining_overs, ' overs of the match. Bengaluru needs 40 runs to win and with 4 wickets left.')
print('Bengaluru has following 4 available batsmen :')
print(*all_batsmen, sep="\n")
print('Current batsmen on strike : ', all_batsmen[0])
print('\n')


def get_over_representation(current_ball):
    global balls_in_an_over
    remainder_o = current_ball % balls_in_an_over
    quotient_o = current_ball // balls_in_an_over
    over_complete = True if remainder_o == 0 else False
    return {
        'over_count': str(quotient_o) + '.' + str(remainder_o),
        'over_complete': over_complete,
        'over_number': quotient_o,
        'ball_count': remainder_o
    }


def logMatchSummary():
    print('\n')
    print("########## MATCH SUMMARY ##########")
    print('Total Runs scored by batting team:', total_runs_scored)
    for k in player_dictionary:
        if k in available_batsmen and player_dictionary[k]['balls'] > 0:
            not_out_sym = '*'
        else:
            not_out_sym = ''
        print(k, '-', player_dictionary[k]['score'], not_out_sym, '(', player_dictionary[k]['balls'], 'balls )')
    exit()


# updating the player dictionary
def update_batsmen_stats(batsmen, run):
    player_dictionary[batsmen]['score'] += run
    player_dictionary[batsmen]['balls'] += 1


# only checking if won or not
def check_score(batsmen, ball, run):
    if total_runs_scored > runs_needed:
        match_commentary(log_case='batting_team_won',
                         data={'batsmen': batsmen, 'current_ball': ball, 'run': run})


def rotate_strike():
    global batsmen
    available_batsmen[0], available_batsmen[1] = available_batsmen[1], available_batsmen[0]
    batsmen = available_batsmen[0]


def match_commentary(log_case, data):
    global batsmen
    over_details = get_over_representation(current_ball=data['current_ball'])
    ball_number = over_details['over_count']
    over_complete = over_details['over_complete']
    over_number = over_details['over_number']
    ball_count = over_details['ball_count']

    if log_case == 'player_out':
        print(ball_number, ':', data['out_batsmen'], 'has been bowled out/caught.', data['new_batsmen'],
              'has now come out to play. He will take the strike.')
        print(data['out_batsmen'], '-', player_dictionary[data['out_batsmen']]['score'], '(',
              player_dictionary[data['out_batsmen']]['balls'], 'balls )')

        print('\n')
    elif log_case == 'team_dismissed':
        print(ball_number, ':', data['out_batsmen'], 'has been bowled out/caught.', 'He scored',
              player_dictionary[data['out_batsmen']]['score'], 'runs.')
        print(data['out_batsmen'], '-', player_dictionary[data['out_batsmen']]['score'], '(',
              player_dictionary[data['out_batsmen']]['balls'], 'balls )')
        print('\n')

        print('The batting team has lost the match by', runs_needed - total_runs_scored, 'runs', 'with',
              (remaining_overs * 6) - (over_number * 6 + ball_count), 'balls remaining')
        logMatchSummary()

    elif log_case == 'strike_change':
        print(ball_number, ':', data['out_batsmen'], 'has scored', data['run'], 'runs.', data['new_batsmen'],
              'is now on strike.')
    elif log_case == 'batting_team_won':
        if data['run'] == 4 or data['run'] == 6:
            print(ball_number, ':', 'It\'s a boundary! ', data['batsmen'], 'has scored', data['run'], 'runs.')
        else:
            print(ball_number, ':', data['batsmen'], 'has scored', data['run'], 'runs.')

        print('\n')
        print('The batting team has won the match by', len(available_batsmen), 'wickets', 'with',
              (remaining_overs * 6) - (over_number * 6 + ball_count), 'balls remaining')
        logMatchSummary()
    elif log_case == 'strike_retain':
        if data['run'] == 4 or data['run'] == 6:
            print(ball_number, ':', 'It\'s a boundary! ', data['batsmen'], 'has scored', data['run'], 'runs.',
                  'He will retain the strike.')
        else:
            print(ball_number, ':', data['batsmen'], 'has scored', data['run'], 'runs.',
                  'He will retain the strike.')

    if over_complete:
        print('\n')
        print('########### OVER SUMMARY ###########')
        print('Team score :', total_runs_scored)
        print('Runs needed to win :', runs_needed - total_runs_scored)
        print('Balls Remaining :', (remaining_overs * 6) - (over_number * 6))
        rotate_strike()
        print('-----', batsmen, 'is now on strike.', '-----')
        print('\n')

        if over_number == remaining_overs:
            print('------ OVERS FINISHED ------')
            print('The batting team has lost the match by', runs_needed - total_runs_scored, 'runs', 'with',
                  (remaining_overs * 6) - (over_number * 6 + ball_count), 'balls remaining')
            logMatchSummary()


def select_batsmen(run, ball):
    global batsmen
    global total_runs_scored
    if run % 2 == 0:
        total_runs_scored += run
        update_batsmen_stats(batsmen, run)

        check_score(batsmen, ball, run)
        match_commentary(log_case='strike_retain',
                         data={'batsmen': batsmen, 'current_ball': ball, 'run': run})
    elif run < 0:
        player_dictionary[batsmen]['balls'] += 1
        out_batsmen = batsmen
        available_batsmen.remove(batsmen)
        if len(available_batsmen) < 2:
            match_commentary(log_case='team_dismissed',
                             data={'out_batsmen': batsmen, 'current_ball': ball})
            exit()
        rotate_strike()
        match_commentary(log_case='player_out',
                         data={'out_batsmen': out_batsmen, 'new_batsmen': batsmen, 'current_ball': ball})
    else:
        total_runs_scored += run
        update_batsmen_stats(batsmen, run)

        check_score(batsmen, ball, run)

        out_batsmen = batsmen
        rotate_strike()
        match_commentary(log_case='strike_change',
                         data={'out_batsmen': out_batsmen, 'new_batsmen': batsmen, 'current_ball': ball, 'run': run})
    return batsmen


def main():
    for var in list(range(total_balls)):
        run_scored = random.choice(player_dictionary[batsmen]['probability'])
        select_batsmen(run=run_scored, ball=var + 1)


if __name__ == '__main__':
    main()
