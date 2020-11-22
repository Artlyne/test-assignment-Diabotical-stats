# CLI приложение чтения статистики игроков в Diabotical через API
[Diabotical API](https://mtricht.github.io/diabotical-api/#/Leaderboard/get_api_v0_stats_leaderboard)
***
В утилите доступны следующие возможности:

- *--mode \<game_mode>* — вывести информацию о всех игроках в данном моде

- *--count \<N>* — ограничить вывод N игроками

- *--user_id \<id>* — найти и вывести информацию о конкретном игроке

- *--country \<country>* — посчитать количество игроков определенной страны
***
### Примеры использования
```
$ poetry run diabotical-stats --mode r_macguffin --count 3
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
$ poetry run diabotical-stats --mode r_macguffin --count 3 --user_id b325363ffe6d46c8840c951b334cc09c
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
$ poetry run diabotical-stats --mode r_macguffin --count 3 --country dk
1
```
