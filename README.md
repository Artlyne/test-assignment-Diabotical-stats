# CLI app for reading player statistics in Diabotical<img src="https://pbs.twimg.com/profile_images/1231999603588947974/sZOe6DPF.png" width="50" height="50">
![Github Actions Status](https://github.com/Artlyne/test-assignment-Diabotical-stats/workflows/Python%20CI/badge.svg)

[Diabotical API](https://mtricht.github.io/diabotical-api/#/Leaderboard/get_api_v0_stats_leaderboard)
***
To install the package, copy the current repository and enter the following command:
```
make install
```
The following features are available in the utility:

- *--mode \<game_mode>* — display information about all players in a given mod

- *--count \<N>* — limit output to N players

- *--user_id \<id>* — find and display information about a specific player

- *--country \<country>* — count the number of players in a certain country
***
### Examples
```
$ diabotical-stats --mode r_macguffin --count 3
{
  "leaderboard": [
    {
      "name": "enesy",
      "country": "dk",
      "match_type": 2,
      "rating": "2246",
      "rank_tier": 40,
      "rank_position": 1,
      "match_count": 48,
      "match_wins": 42
    },
    {
      "name": "Cookk1",
      "country": "",
      "match_type": 2,
      "rating": "2216",
      "rank_tier": 40,
      "rank_position": 2,
      "match_count": 34,
      "match_wins": 30
    },
    {
      "name": "absoQL",
      "country": "de",
      "match_type": 2,
      "rating": "2186",
      "rank_tier": 40,
      "rank_position": null,
      "match_count": 109,
      "match_wins": 78
    }
  ]
}
```
```
$ diabotical-stats --mode r_macguffin --count 3 --user_id b325363ffe6d46c8840c951b334cc09c
{
  "name": "enesy",
  "country": "dk",
  "match_type": 2,
  "rating": "2246",
  "rank_tier": 40,
  "rank_position": 1,
  "match_count": 48,
  "match_wins": 42
}
```
```
$ diabotical-stats --mode r_macguffin --count 3 --country dk
1
```
