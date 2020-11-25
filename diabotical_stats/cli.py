import argparse

GAME_MODES = ('r_macguffin', 'r_wo', 'r_rocket_arena_2', 'r_shaft_arena_1',
              'r_ca_2', 'r_ca_1')


def check_positive(x):
    value = int(x)
    if value < 0:
        raise argparse.ArgumentTypeError('Only positive numbers available.')
    return value


def parser():
    parser = argparse.ArgumentParser(description='Get players stats from \
                                        game Diabotical')
    parser.add_argument('--mode', choices=GAME_MODES, required=True,
                        help='choose game mode')
    parser.add_argument('--count', type=check_positive,
                        help='specify the number of records to output')
    parser.add_argument('--user_id',
                        help='specify the user id you want to find')
    parser.add_argument('--country',
                        help='count the number of players in a given country')
    return parser
