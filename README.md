PROJECT 
ETL (Extract, Transform, Load) Automation for Complaint Data 

This Python script serves as a dynamic ETL (Extract, Transform, Load) processor for CSV files containing complaint data. 
The script automatically extracts creation dates from file names, filters files based on the current date, reads CSV files, aggregates and groups data, and finally, loads the transformed data into a specified destination CSV file.

Installation:
•	Ensure that Python is installed on your system.
•	Install required dependencies using : pip install pandas

Project Structure:
1.	File Naming Convention:
The script assumes that files in the specified directory follow a specific naming convention, including the creation timestamp.

Workflow:
•	The script dynamically extracts creation dates from file names.
•	It identifies files created on the current date.
•	Reads the relevant CSV file based on the current date.
•	Performs data aggregation based on specified columns.
•	Saves the aggregated data into a user-defined destination CSV file.

Dependencies:
The script requires the Pandas library for data manipulation.

Usage:
•	Place CSV files in the specified directory with the required naming convention.
•	Run the script, and it will automatically process the files for the current date.
•	Customize the file paths as indicated in the comments.

Error Handling:
The script includes error handling for file availability and general exceptions during CSV reading and writing.

Output:
The final aggregated data is saved in a user-defined destination CSV file.

Configuration:
•	Open the script and set the appropriate file paths:
•	Specify the folder path containing CSV files.
•	Specify the destination file path for the final aggregated data.

Output:
Check the specified destination CSV file for the final aggregated data.
