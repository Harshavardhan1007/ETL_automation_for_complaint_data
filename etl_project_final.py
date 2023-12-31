import pandas as pd
import os
import datetime
from etl_project import (
    get_date_with_file_name,
    get_current_date_file,
    read_csv_file,
    get_state_wise_records,
    convert_df_to_csv)

list_file=os.listdir("Enter folder path to get file names in that folder")
file_name_with_dates=get_date_with_file_name(list_file)

file_name_list=get_current_date_file(file_name_with_dates)
get_file_name=str(file_name_list).replace("['","").replace("']","")

input_file_path=f"Enter the file path/{get_file_name}"
df=read_csv_file(input_file_path)

grouped_state_wise_df=get_state_wise_records(state_wise_df = df,col=['State Name','Product Name','Sub Product'])

file_path="Enter the destination file path.csv"
convert_df_to_csv(file_path,grouped_state_wise_df)