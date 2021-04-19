import pandas as pd 
import numpy as np


PATH_ROSTER = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\14th_2021.xlsx'
PATH_SALARY = 'D:\\Run Analysis\\BLOB_STORAGE\\Driver_weekly_timesheet\\processed_timesheet\\14th_2021.csv'

# 71641 total salary

df_sal = pd.read_csv(PATH_SALARY)
df_ros = pd.read_excel(PATH_ROSTER)
# how='left'
df_sal_ros = pd.merge(df_ros, df_sal , left_on='Primary_employeeID',right_on='EmployeeID_y')

df_sal_ros[[
    'Date',
    'Run_type',
    'Primary_employeeID',
    'Secondary_employeeID',
    'Primary_driver_Name',
    'Secondary_Driver_Name',
    'Primary_route',
    'Satellite_Route_1',
    'Satellite_Route_2',
    'Primary_truck',
    'Alternative_Truck',
    'Subcontracted_From/Special_Client',
    'Total_hour'
]]

occurence_per_runs_ = (df_sal_ros
 .groupby(['Primary_employeeID', 'Primary_route','Total_hour'])['Run_type']
 .count()
 .reset_index())

total_runs = df_sal_ros.groupby('Primary_employeeID')['Run_type'].count().reset_index()

df_1 = pd.merge(occurence_per_runs_, total_runs, on='Primary_employeeID', how='left')
# df_ros.info()
# series_1 = df_sal_ros.groupby(['Primary_employeeID', 'Total_hour'])['Run_type'].count().reset_index()

# df_sal_ros
# df_1.groupby/('Primary_employeeID')['Total_hour'].count()
df_ab= df_1.drop_duplicates(subset='Primary_employeeID',keep='first')
df_ab