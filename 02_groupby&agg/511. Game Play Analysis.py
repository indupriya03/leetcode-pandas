#511. Game Play Analysis I

"""
Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+

Task:
Find the first login date for each player.

Return:
DataFrame with columns ['player_id', 'first_login']
"""
import pandas as pd

def game_analysis(activity_df: pd.DataFrame) -> pd.DataFrame:
    """
    Find first login date for each player.
    :param activity_df: DataFrame with Columns ['player_id','device_id','event_date','games_played']
    :return: DataFrame with columns ['player_id','first_login']
    """
    return activity_df.groupby('player_id',as_index=False)['event_date'].min().rename(columns={'event_date':'first_login'})

if __name__ == '__main__':
    #Sample Activity_df Table
    Activity_df=pd.DataFrame({
        'player_id':[1,1,2,3,3],
        'device_id':[2,2,3,1,4],
        'event_date':['2016-03-01','2016-05-02','2017-06-25','2016-03-02','2018-07-03'],
        'games_played':[5,6,1,0,5]
    })
    # Compute first login dates
    print(game_analysis(Activity_df))