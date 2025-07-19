import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    #condition
    condition = (df['employee_id'] % 2 != 0) & (~df['name'].str.startswith('M'))

    #calculate bonus
    df['bonus'] = df['salary'].where(condition,0)
    return df[['employee_id','bonus']].sort_values(by='employee_id')
    