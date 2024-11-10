import pandas as pd

def convert_to_datetime(file1: pd.DataFrame, file2: pd.DataFrame) -> list:
	print(list(file1.columns))
	file1['time'] = pd.to_datetime(file1['time'], errors='coerce')
	
	print(list(file2.columns))
	file2['time'] = pd.to_datetime(file2['time'], errors='coerce')

	return [file1, file2]


def drop_columns(file: pd.DataFrame, default_drop: str) -> pd.DataFrame:
	headers_file = list(file.columns)
	print(headers_file)
	to_keep: str = input("Give us the index of the columns to remove. (e.g. input \"23\" to keep column remove 2 and 3)")
	if (to_keep == ""):
		to_keep = default_drop
	how_many: int = len(to_keep)
	while (how_many > 0):
		file = file.drop([headers_file[int(to_keep[how_many - 1])]], axis=1)
		how_many -= 1
	columns_names = list(file.columns)
	print(columns_names)
	file = file.rename(columns={columns_names[0]:"time"})
	file = file.rename(columns={columns_names[1]:"data"})
	return file
 
def clean_up(file1: pd.DataFrame, file2: pd.DataFrame) -> list:
	file1 = drop_columns(file1,"0134" )
	file2 = drop_columns(file2, "01")

	return [file1, file2]


