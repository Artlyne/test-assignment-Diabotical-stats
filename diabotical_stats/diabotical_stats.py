import requests
import json


def get_leaderboard(url: str, parameters: dict) -> list:
    data = requests.get(url, params=parameters).json()
    return data.get('leaderboard')


def remove_userid(leaderboard: list) -> list:
    for user_stat in leaderboard:
        user_stat.pop('user_id')
    return leaderboard


def convert_to_json(data: list) -> str:
    return json.dumps(data, indent=2)


def get_stats(url: str, parameters: dict, count: int) -> str:
    return convert_to_json(remove_userid(
        get_leaderboard(url, parameters)[:count]))
