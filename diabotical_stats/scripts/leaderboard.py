#!/usr/bin/env python3
import json
from diabotical_stats.cli import parse_args
from diabotical_stats.diabotical_stats import count_players_by_country
from diabotical_stats.diabotical_stats import get_leaderboard, get_user
from diabotical_stats.diabotical_stats import remove_userids


URL = 'https://www.diabotical.com/api/v0/stats/leaderboard?'
PARAMETERS = {'mode': parse_args().mode}


def main():
    leaderboard = get_leaderboard(URL, PARAMETERS, parse_args().count)

    if parse_args().user_id:
        result = get_user(leaderboard, parse_args().user_id)
    elif parse_args().country:
        result = count_players_by_country(leaderboard, parse_args().country)
    else:
        result = remove_userids(leaderboard)

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
