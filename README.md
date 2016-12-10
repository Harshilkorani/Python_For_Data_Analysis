##PYTHON FINAL PROJECT

* Raw data is collected from http://cricsheet.org/
* Raw data consists of 2 files matches.csv & deliveries.csv
* Matches.csv consists of following columns & data for all 577 matches held till date:

![matches](https://cloud.githubusercontent.com/assets/12143009/21074980/29cbd1e4-bed5-11e6-99f7-f34b0e96c649.PNG)

* Deliveries.csv consists of following columns & ball by ball data for each match held till date:

![deliveries](https://cloud.githubusercontent.com/assets/12143009/21075002/92e64754-bed5-11e6-9584-3759332e982e.PNG)

* First step done was to read the data into a data frame.
```
sample code:
path = "C:/PYTHON/pythonFinalProject/rawDataPythonIPL"
all_matches_df = pd.read_csv(path+"\matches.csv")
all_matches_df.head(2)
```

* Second step was to find the aggregate scores for each match

![aggregate_score](https://cloud.githubusercontent.com/assets/12143009/21075050/8e3401d2-bed6-11e6-85b2-04ebda918845.PNG)

* Merge the team scores for each match with the matches, so adding new columns to the all matches data

* After this, adding new column which identifies the match type for each match as a Pre-qualifier, Qualifier, Eliminator & Final

![match_type](https://cloud.githubusercontent.com/assets/12143009/21075078/5aa9ea2e-bed7-11e6-8ec8-3941f3dfa10c.PNG)

* After data pre-processing, time to perform some analysis:

###ANALYSIS 1: Team Wins in different Cities in various IPL Seasons

![wins_per_city](https://cloud.githubusercontent.com/assets/12143009/21075113/013af3f6-bed8-11e6-8d2b-cb714f90ff04.PNG)


![total_wins_per_city](https://cloud.githubusercontent.com/assets/12143009/21075123/334732ce-bed8-11e6-8f45-e244cbfcb7ea.png)


###ANALYSIS 2: Toss Decision & Impact in IPL across seasons for various teams

![toss](https://cloud.githubusercontent.com/assets/12143009/21075145/a5d8ad18-bed8-11e6-937a-e0d554db932e.PNG)

![toss1](https://cloud.githubusercontent.com/assets/12143009/21075155/08b4b8be-bed9-11e6-97a8-2fd813f035a1.PNG)

![toss_winner_is_match_winner_for_teams](https://cloud.githubusercontent.com/assets/12143009/21075149/cf11c9f8-bed8-11e6-8188-f168cc18ae4a.png)

###ANALYSIS 3a : Team which handle their nerves under pressure ?

![close_matches](https://cloud.githubusercontent.com/assets/12143009/21075168/6b67ae6c-bed9-11e6-8c90-246e84fa305c.PNG)

![team_winning_close_matches](https://cloud.githubusercontent.com/assets/12143009/21075174/91d5428a-bed9-11e6-8884-0bd6569e8522.png)

###ANALYSIS 3b: No. of times, Teams dominated their opposition with big victories

![big_margins](https://cloud.githubusercontent.com/assets/12143009/21075191/dcd19fea-bed9-11e6-83cc-1585a7afe6de.PNG)

![team_winning_big_margins](https://cloud.githubusercontent.com/assets/12143009/21075199/f532bb28-bed9-11e6-8b61-5c255d78efce.png)

###ANALYSIS 4: Top 5 Batsman

![top5](https://cloud.githubusercontent.com/assets/12143009/21075230/70cd4802-beda-11e6-8cc4-bc2187581024.PNG)

![top_5_batsman_runs_per_season](https://cloud.githubusercontent.com/assets/12143009/21075237/8a4e9ed4-beda-11e6-93b0-35ec2b830406.png)


###ANALYSIS 5: Player Comparison (Player 1 vs Player 2, in terms of runs scored, balls faced, strike rate)

* Calculated all the batsman aggregates like runs scored per match, balls face, 4s scored, 6s scored, strike rate, dismissal-kind

![players_comparison_by_balls_faced](https://cloud.githubusercontent.com/assets/12143009/21075260/05287328-bedb-11e6-8c94-92e5c7cbe1c0.png)

![players_comparison_by_runs](https://cloud.githubusercontent.com/assets/12143009/21075261/0a49e850-bedb-11e6-87d4-3a6fe4403e01.png)

![players_comparison_by_strike_rate](https://cloud.githubusercontent.com/assets/12143009/21075262/0eb2608e-bedb-11e6-94b0-7fb7195bf088.png)








