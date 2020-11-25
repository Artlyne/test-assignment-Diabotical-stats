import requests
import json

URL = 'https://www.diabotical.com/api/v0/stats/leaderboard?'


def get_leaderboard(mode: dict, count: int) -> list:
    try:
        response = requests.get(URL, params={'mode': mode}).json()
        return response.get('leaderboard')[:count]
    except requests.exceptions.RequestException:
        print("Service isn't available right now.")


def get_user(leaderboard: list, user_id: str) -> dict:
    for user in leaderboard:
        if user['user_id'] == user_id:
            # making new user without key 'user_id'
            return {k: v for k, v in user.items() if k != 'user_id'}


def remove_userids(leaderboard: list) -> list:
    copyed_leaderboard = leaderboard.copy()
    for user in copyed_leaderboard:
        user.pop('user_id')
    return copyed_leaderboard


def count_players_by_country(leaderboard: list, country: str) -> int:
    counter = 0
    for user in leaderboard:
        if user['country'] == country:
            counter += 1
    return counter


def get_stats(mode: str, count: int, user_id: str, country: str) -> str:
    try:
        leaderboard = get_leaderboard(mode, count)

        if user_id:
            result = get_user(leaderboard, user_id)
            if result is None:
                return f"User with user_id '{user_id}' not found"
        elif country:
            result = count_players_by_country(leaderboard, country)
        else:
            result = {'leaderboard': remove_userids(leaderboard)}

        return json.dumps(result, indent=2)

    except (AttributeError, TypeError):
        return 'Something went wrong! Please try again later.'
