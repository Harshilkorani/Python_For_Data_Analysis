##PYTHON FINAL PROJECT

# IPL Data Analysis
![vivo-ipl-2016-logos](https://cloud.githubusercontent.com/assets/12143009/21077436/631cfbe6-bf19-11e6-8889-72b7adda39cc.jpg)

## Content:

 * Introduction about data 
 
 * Pre-processing steps
 
 * Analysis 1 : Season wise wins for each team at different venue
  * Result : Stacked Bar Chart
  
 * Analysis 2 : Toss Impact on different teams across seasons
  * Result : Grouped Bar Plot
  
 * Analysis 3a : Teams handling their nerves successfully
  * Result : Bar Plot
 
 * Analysis 3b : Teams dominating their opposition
  * Result : Bar Plot
  
 * Analysis 4 : Top 5 batsman performances across seasons
  * Result : Point Plot Chart
  
 * Analysis 5 : Dynamic Player Comparison against runs scored, strike rate
  * Result : Grouped Bar Chart


## Introduction
**************************************************************************************************************************************
* Raw data is collected from http://cricsheet.org/
* Raw data consists of 2 files matches.csv & deliveries.csv
* Matches.csv consists of following columns & data for all 577 matches held till date:

####Matches.csv
![matches](https://cloud.githubusercontent.com/assets/12143009/21074980/29cbd1e4-bed5-11e6-99f7-f34b0e96c649.PNG)


* Deliveries.csv consists of following columns & ball by ball data for each match held till date:

####Deliveries.csv
![deliveries](https://cloud.githubusercontent.com/assets/12143009/21075002/92e64754-bed5-11e6-9584-3759332e982e.PNG)


* Sample code to read csv data into a data frame.
```python 
sample code:
path = "C:/PYTHON/pythonFinalProject/rawDataPythonIPL"
all_matches_df = pd.read_csv(path+"\matches.csv")
all_matches_df.head(2)
```


* Aggregate Total scores, team extras for each match


####Total Team Score
![aggregate_score](https://cloud.githubusercontent.com/assets/12143009/21077857/7c0a66a8-bf27-11e6-9060-9920547ef46f.PNG)


####Total Team Extras
![team_extras](https://cloud.githubusercontent.com/assets/12143009/21077495/768daac0-bf1b-11e6-8d37-fcc2cd4c691f.PNG)


* Merge the team scores for each match with the matches, so adding new columns to the all matches data

* Adding new column which identifies the match type for each match as a Pre-qualifier, Qualifier, Eliminator & Final
```python 
sample code:
for year in range(2008,2017):
    fourth_last_match_in_each_season = all_matches_df[all_matches_df["season"] == year][-4:].index.values[0]
    third_last_match_in_each_season = fourth_last_match_in_each_season + 1
    second_last_match_in_each_season = third_last_match_in_each_season + 1
    last_match_in_each_season = second_last_match_in_each_season + 1
    
    all_matches_df = all_matches_df.set_value(fourth_last_match_in_each_season, "match-type" , "Qualifier-1")
    all_matches_df = all_matches_df.set_value(third_last_match_in_each_season, "match-type" , "Eliminator")
    all_matches_df = all_matches_df.set_value(second_last_match_in_each_season, "match-type" , "Qualifier-2")
    all_matches_df = all_matches_df.set_value(last_match_in_each_season, "match-type" , "Final")
```


## ANALYSIS 1: Team Wins in different Cities in various IPL Seasons
**************************************************************************************************************************************

####Code to get team wins per city data:
![wins_per_city](https://cloud.githubusercontent.com/assets/12143009/21075113/013af3f6-bed8-11e6-8d2b-cb714f90ff04.PNG)


####Graph:
![total_wins_per_city](https://cloud.githubusercontent.com/assets/12143009/21075123/334732ce-bed8-11e6-8f45-e244cbfcb7ea.png)




## ANALYSIS 2: Toss Decision & Impact in IPL across seasons for various teams
**************************************************************************************************************************************

####Code to get toss winners data:
![toss](https://cloud.githubusercontent.com/assets/12143009/21075145/a5d8ad18-bed8-11e6-937a-e0d554db932e.PNG)


####Graph 1:
![toss1](https://cloud.githubusercontent.com/assets/12143009/21077917/4b0a3f86-bf29-11e6-9e1b-be9434f1f149.PNG)


####Graph 2:
![toss_winner_is_match_winner_for_teams](https://cloud.githubusercontent.com/assets/12143009/21077397/1b957236-bf18-11e6-8022-0f2ad0aa273c.png)



## ANALYSIS 3a : Team which handle their nerves under pressure ?
**************************************************************************************************************************************

####Code to get teams which won close matches:
![close_matches](https://cloud.githubusercontent.com/assets/12143009/21075168/6b67ae6c-bed9-11e6-8c90-246e84fa305c.PNG)


####Graph:
![team_winning_close_matches](https://cloud.githubusercontent.com/assets/12143009/21075174/91d5428a-bed9-11e6-8884-0bd6569e8522.png)



## ANALYSIS 3b: No. of times, Teams dominated their opposition with big victories
**************************************************************************************************************************************

####Code to get teams winning with big margins
![big_margins](https://cloud.githubusercontent.com/assets/12143009/21075191/dcd19fea-bed9-11e6-83cc-1585a7afe6de.PNG)


####Graph:
![team_winning_big_margins](https://cloud.githubusercontent.com/assets/12143009/21075199/f532bb28-bed9-11e6-8b61-5c255d78efce.png)



## ANALYSIS 4: Top 5 Batsman
**************************************************************************************************************************************

####Code to get top 5 batsman:
![top5](https://cloud.githubusercontent.com/assets/12143009/21075230/70cd4802-beda-11e6-8cc4-bc2187581024.PNG)


####Graph:
![top_5_batsman_runs_per_season](https://cloud.githubusercontent.com/assets/12143009/21075237/8a4e9ed4-beda-11e6-93b0-35ec2b830406.png)


## ANALYSIS 5: Player Comparison (Player 1 vs Player 2, in terms of runs scored, balls faced, strike rate)
**************************************************************************************************************************************

* Calculated all the batsman aggregates like runs scored per match, balls face, 4s scored, 6s scored, strike rate, dismissal-kind



match_id | inning | batting_team | batsman | batsman_runs | balls_faced | Strike-Rate | More-Than-30 | More-Than-50 | More-Than-100 | 4s | 6s | dismissal_kind | fielder
----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- 
1 | 1 | Kolkata Knight Riders|BB McCullum|158|73.0|216.44|1|1|1|10|13|0|0
1 | 1 | Kolkata Knight Riders|DJ Hussey|12|12.0|100.00|0|0|0|1|0|caught|CL White




####Graph 1: Player Comparison By Runs
![players_comparison_by_balls_faced](https://cloud.githubusercontent.com/assets/12143009/21075260/05287328-bedb-11e6-8c94-92e5c7cbe1c0.png)

####Graph 2: Player Comparison By Balls Faced
![players_comparison_by_runs](https://cloud.githubusercontent.com/assets/12143009/21075261/0a49e850-bedb-11e6-87d4-3a6fe4403e01.png)


####Graph 3: Player Comparison By Strike_Rate
![players_comparison_by_strike_rate](https://cloud.githubusercontent.com/assets/12143009/21075262/0eb2608e-bedb-11e6-94b0-7fb7195bf088.png)








