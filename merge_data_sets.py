import pandas as pd
import numpy as np

def convert_to_datetime(file1: pd.DataFrame, file2: pd.DataFrame, default_select: str):
	select1 = input("What is the name of the column containing time ? ")
	print(list(file1.columns))
	if (select1 == ""):
		select1 = default_select
	file1[select1] = pd.to_datetime(file1[select1], errors='coerce')
	
	select2 = input("What is the name of the column containing time ? ")
	print(list(file2.columns))
	if (select2 == ""):
		select2 = default_select
	file2[select2] = pd.to_datetime(file2[select2], errors='coerce')
	
	print(file1)
	return [file1, file2]

def get_date_limits(file1: pd.DataFrame, file2: pd.DataFrame) -> list:
	first_year_file1 = file1['Day'].iloc[0].year
	first_year_file2 = file2['Day'].iloc[0].year

	last_year_file1 = file1['Day'].iloc[-1].year
	last_year_file2 = file2['Day'].iloc[-1].year

	return [first_year_file1, first_year_file2, last_year_file1, last_year_file2]

def initialise_merged_data_set(limits: list) -> np.array:
	if (limits[0] < limits[1]):
		start = limits[1]
	else:
		start = limits[0]

	if (limits[2] < limits[3]):
		end = limits[2]
	else:
		end = limits[3]
	number_of_year = end - start + 1
	merged_data_set = np.zeros((141, 3))

	n = 0
	while (start < end + 1):
		merged_data_set[n][0] = start
		start += 1
		n += 1

	return (merged_data_set)

