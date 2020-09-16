import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df_deliveries=pd.read_csv('ipl/deliveries.csv')
df_matches=pd.read_csv('ipl/matches.csv')


print(df_deliveries.head())
print('\n')
print(df_matches.head())
print('\n')



print(df_deliveries.describe())
print('\n')
print(df_matches.describe())
print('\n')


print(df_deliveries.info())
print('\n')
print(df_matches.info())
print('\n')



#Check For Null Values :

print('Null Values Of Matches Dataframe : \n',df_matches.isnull().sum())
print('\n')
print('Null Values Of Deliveries Dataframe : \n',df_deliveries.isnull().sum())



print(df_matches['umpire3'].unique())
print(df_matches['umpire3'].nunique(dropna=False))
df2=df_matches.drop(['umpire3'],axis=1)


print("Basic Overview Of Matches Dataset : \n")
print('Number Of Matches Played :',df_matches.shape[0])
print("Number Of Seasons Played : ",df_matches['season'].value_counts().nunique())
print("Top 10 Prominent Players of IPL : \n", df_matches['player_of_match'].value_counts()[:10])
print("Most Winning Team and Number Of Matches: \n",df_matches['winner'].value_counts())
print("Most Winning Team: \n",df_matches['winner'].value_counts().idxmax())
print("Player Of The Match & Number Of Matches : \n",df_matches['player_of_match'].value_counts())
print("Player Of The Match For Max . Matches : \n",df_matches['player_of_match'].value_counts().idxmax())

print('\n')
#Some Condtional Filtering :
big_margin=df_matches[(df_matches['win_by_runs']>=100) | (df_matches['win_by_wickets']>=8)]
print(big_margin.winner.value_counts())

print("Number Of Seasons Played IN Different Cities : \n",df_matches.groupby('city')['season'].nunique())
print("Number Of Winners In Different Cities \n",df_matches.groupby('city')['winner'].nunique())
print("Winners in Cities \n",df_matches.groupby('city')['winner'].value_counts())

print("Match where team won by highest runs",df_matches.iloc[df_matches['win_by_runs'].idxmax()])
print('\n')
print("Match where team won by highest wickets",df_matches.iloc[df_matches['win_by_wickets'].idxmax()])

print("Basic Overview of Deliveries Dataset : \n")
print(df_deliveries.info())

print("Number Of Innings And Their Counts : \n",df_deliveries['inning'].value_counts())
print("Batting Team 's Max Counts :",df_deliveries['batting_team'].value_counts())
print("Number Of Super Over Matches  : \n",df_deliveries['is_super_over'].value_counts())

