# 584. Find Customer Referee
"""
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+

In SQL, id is the primary key column for this table.
Each row indicates the id of a customer, their name,
and the id of the customer who referred them.

Find the names of customers who are either:
1. Referred by any customer with id != 2
2. Not referred by any customer
"""
import pandas as pd
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    """
    Return the names of customers who are either:
    1. Not referred by any customer, or
    2. Referred by a customer whose id is not 2
    :param: DataFrame containing customer details
    :return: DataFrame with column 'name'
    """
    # filtered the customers satisfying the conditions
    filtered=customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())]
    # return the dataframe with column 'name'
    return filtered[['name']]
if __name__ == "__main__":
    # Sample Customer Table
    Customer_df=pd.DataFrame({
        'id' : [1,2,3,4,5,6],
        'name' : ['Will','Jane','Alex','Bill','Zack','Mark'],
        'referee_id' : [None,None,2,None,1,2]
    })
    print(find_customer_referee(Customer_df))