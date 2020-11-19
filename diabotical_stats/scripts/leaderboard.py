#!/usr/bin/env python3
from diabotical_stats.cli import parse_args
from diabotical_stats.diabotical_stats import get_stats


URL = 'https://www.diabotical.com/api/v0/stats/leaderboard?'
PARAMETERS = {'mode': parse_args().mode}


def main():
    print(get_stats(URL, PARAMETERS, parse_args().count))


if __name__ == '__main__':
    main()
