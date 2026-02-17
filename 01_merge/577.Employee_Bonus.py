"""
LeetCode 577 - Employee Bonus

Problem:
Report the name and bonus amount of each employee who:
1. Has a bonus less than 1000, OR
2. Did not receive any bonus.

Approach:
- Perform a LEFT JOIN between Employee and Bonus tables
- Filter employees based on bonus conditions
"""
import pandas as pd
def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """
     Returns employees whose bonus is less than 1000 or who did not receive any bonus.
     :param employee: DataFrame containing employee details
     :param bonus: DataFrame containing employee bonus details
     :return: DataFrame with columns ['name', 'bonus']
     """
    # Merge the bonus table with employee table
    merged=employee.merge(bonus, on='empId',how='left')
    # Filter the employees who have no bonus or less than 1000
    merged=merged[(merged['bonus']<1000) | (merged['bonus'].isnull())]
    # Return the filtered employees name and bonus
    return merged[['name','bonus']]

if __name__=='__main__':
    # sample employee table
    Employee_df=pd.DataFrame({
        'empId' : [3,1,2,4],
        'name' : ['Brad','John','Dan','Thomas'],
        'supervisor' : [None,3,3,3],
        'salary' : [4000,1000,2000,4000]

    })
    #sample bonus table
    Bonus_df=pd.DataFrame({
        'empId' : [2,4],
        'bonus' : [500,2000]
    })
    print(employee_bonus(Employee_df,Bonus_df))