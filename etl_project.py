import pandas as pd
import os 
import datetime 


def get_date_with_file_name(list_file):
    datetime_file=[]
    for i in list_file:
        file_created=os.path.getctime(f"Enter file path/{i}")
        dt_c = datetime.datetime.fromtimestamp(file_created)
        datetime_file.append(i+"-"+dt_c.strftime('%Y/%m/%d %H:%M:%S')) 
    return datetime_file

list_file=os.listdir("Enter folder path to get file name")
file_name_with_dates=get_date_with_file_name(list_file)

def get_current_date_file(file_name_with_dates):
    file_matching_with_date=[k for k in file_name_with_dates if datetime.datetime.today().strftime('%Y/%m/%d') in k]
    file_name_only=[k.split('-')[0] for k in file_matching_with_date]
    return file_name_only

file_name_list=get_current_date_file(file_name_with_dates)
get_file_name=str(file_name_list).replace("['","").replace("']","")


def read_csv_file(input_file_path):
    try:
        csv_to_df=pd.read_csv(input_file_path)
        return csv_to_df
    except FileNotFoundError as os:
        print("file is not available",os)
    except Exception as e:
        print("The error: ",e)

input_file_path=f"Enter the file path/{get_file_name}"
df=read_csv_file(input_file_path)

def get_state_wise_records(state_wise_df,col):
    grouped_df=state_wise_df.groupby(col)['Complaint ID'].agg(['count'])
    grouped_df.rename(columns={'count':'total_complaints'},inplace=True)
    return(grouped_df)

grouped_state_wise_df=get_state_wise_records(state_wise_df=df,col=['State Name','Product Name','Sub Product'])


def convert_df_to_csv(file_path,grouped_state_wise_df):
    try:
        with open(file_path,mode='a') as append_df:
            grouped_state_wise_df.to_csv(append_df,header=True)
    except Exception as e:
        print("error is ",e)
    else:
        print("File is sucessful loaded in the given file path")

file_path="Enter the destination file path.csv"
convert_df_to_csv(file_path,grouped_state_wise_df)