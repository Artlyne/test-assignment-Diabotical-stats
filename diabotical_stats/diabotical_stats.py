import requests


def get_leaderboard(url: str, parameters: dict, count: int) -> list:
    data = requests.get(url, params=parameters).json()
    return data.get('leaderboard')[:count]


def get_user(leaderboard: list, user_id: str):
    for user in leaderboard:
        if user_id == user['user_id']:
            user.pop('user_id')
            return user
    else:
        return 'No such user found! Please try again.'


def remove_userids(leaderboard: list) -> list:
    for user_stat in leaderboard:
        user_stat.pop('user_id')
    return leaderboard


def count_players_by_country(leaderboard: list, country: str) -> int:
    counter = 0
    for user in leaderboard:
        if user['country'] == country:
            counter += 1
    return counter
