#!/usr/bin/env python3
from diabotical_stats.cli import parse_args
from diabotical_stats.diabotical_stats import get_stats, get_user


URL = 'https://www.diabotical.com/api/v0/stats/leaderboard?'
PARAMETERS = {'mode': parse_args().mode}


def main():
    if parse_args().user_id:
        print(get_user(URL, PARAMETERS, parse_args().count,
                       parse_args().user_id))
    else:
        print(get_stats(URL, PARAMETERS, parse_args().count))


if __name__ == '__main__':
    main()
