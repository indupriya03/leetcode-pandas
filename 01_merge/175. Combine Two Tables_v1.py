"""
Problem: Combine Two Tables
Source: LeetCode (Pandas)
Difficulty: Easy

Task:
Report firstName, lastName, city, and state of each person in the Person table.
If a person has no address in Address table, city and state should be null.

Approach:
- Use pd.merge() with how='left' to include all persons
- Select only the required columns in the result
"""

import pandas as pd

def combine_two_tables(person_df,address_df):
    """
    Combine person and address tables to report firstName, lastName,city and state
    :param person_df: DataFrame with columns ['personId','lastName','firstName']
    :param address_df: DataFrame with columns ['addressId','personId','city','state']
    :return: DataFrame with columns ['firstName','lastName','city','state']
    """
    address_df=address_df[['personId','city','state']]
    merged_df=person_df.merge(address_df,on='personId',how='left')
    return merged_df[['firstName','lastName','city','state']]
if __name__=='__main__':
    #sample Person table
    person_data=[
        [1,'Wang','Allen'],
        [2,'Alice','Bob']
    ]
    person_df=pd.DataFrame(person_data,columns=['personId','lastName','firstName'])

    #sample Address table
    address_data=[
        [1,2,'New York City','New York'],
        [1,3,'Leetcode','California']
    ]
    address_df=pd.DataFrame(address_data,columns=['addressId','personId','city','state'])

    #combine tables
    result_df=combine_two_tables(person_df,address_df)
    print(result_df)

