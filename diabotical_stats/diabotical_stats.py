import requests
import json


def get_leaderboard(url: str, parameters: dict, count: int) -> list:
    data = requests.get(url, params=parameters).json()
    return data.get('leaderboard')[:count]


def remove_userids(leaderboard: list) -> list:
    for user_stat in leaderboard:
        user_stat.pop('user_id')
    return leaderboard


def convert_to_json(data: list) -> str:
    return json.dumps(data, indent=2)


def get_stats(url: str, parameters: dict, count: int) -> str:
    leaderboard = remove_userids(get_leaderboard(url, parameters, count))
    return convert_to_json(leaderboard)


def find_user(leaderboard: list, user_id: str):
    for user in leaderboard:
        if user_id == user['user_id']:
            user.pop('user_id')
            return user
    else:
        return 'No such user found! Please try again.'


def get_user(url: str, parameters: dict, count: int, user_id: str) -> str:
    leaderboard = get_leaderboard(url, parameters, count)
    user = find_user(leaderboard, user_id)
    return convert_to_json(user)
