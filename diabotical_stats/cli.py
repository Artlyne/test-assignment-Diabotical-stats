import argparse

GAME_MODES = ('r_macguffin', 'r_wo', 'r_rocket_arena_2', 'r_shaft_arena_1',
              'r_ca_2', 'r_ca_1')


def parse_args():
    parser = argparse.ArgumentParser(description='Get players stats from \
                                        game Diabotical')
    parser.add_argument('--mode', choices=GAME_MODES, required=True,
                        help='choose game mode')
    parser.add_argument('--count', type=int,
                        help='specify the number of records to output')
    args = parser.parse_args()
    return args
