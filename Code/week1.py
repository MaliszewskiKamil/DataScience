import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

football_df = pd.read_csv('football_results.csv')

teams_home = football_df['home']
teams_away = football_df['away']

#teams_away_never_home = football_df.loc[~football_df['away'].isin(teams_home)]
#print(teams_away_never_home.drop_duplicates(subset=['away']))

#teams_away_never_home = football_df[football_df[]]
#teams_home_never_away = football_df.loc[~football_df['home'].isin(teams_away)]
#print(teams_home_never_away.drop_duplicates(subset=['home']))

football_df['home_won'] = football_df.apply(lambda x: 1 if x['gh'] > x['ga'] else 0, axis=1)
#football_df['home_draws'] = football_df.apply(lambda x: 1 if x['gh'] == x['ga'] else 0, axis=1)
#football_df['home_loses'] = football_df.apply(lambda x: 1 if x['gh'] < x['ga'] else 0, axis=1)

print(football_df[['home', 'away','gh', 'ga' ,'home_won']].head())


team_stats = football_df.groupby('home')['home_won'].agg(Sum=np.sum, Count=np.size).sort_values('Sum', ascending=False)
#team_stats['draws'] = football_df.groupby('home')['home_draws'].agg(SumDraw=np.sum, Count=np.size).sort_values('Sum', ascending=False)
#team_stats = football_df.groupby('home')['home_loses'].agg(SumLose=np.sum, Count=np.size).sort_values('Sum', ascending=False)
team_stats['pers_home_win'] = team_stats.apply(lambda x: (x['Sum']/x['Count']) if x['Count'] >= 50 else 0, axis=1)
team_stats['pers_home_not_won'] = team_stats.apply(lambda x: 1-x['pers_home_win'] if x['Count'] >= 50 else 0, axis=1)
print(team_stats[team_stats['Count']>500].sort_values('pers_home_win', ascending=False))

team_stats[team_stats['Count'] > 500].sort_values('pers_home_win', ascending=False).head(7).plot(kind='bar', use_index=True, y=['pers_home_win', 'pers_home_not_won'], label=['win', 'not_won'], stacked=True, rot=45)

plt.show()