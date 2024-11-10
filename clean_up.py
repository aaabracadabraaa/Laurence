import pandas as pd


def drop_columns(file: pd.DataFrame) -> None:
	headers_file = list(file.columns)
	print(headers_file)
	to_keep: str = input("Give us the index of the columns to remove. (e.g. input \"23\" to keep column remove 2 and 3)")
	how_many: int = len(to_keep)
	while (how_many > 0):
		file = file.drop([headers_file[int(to_keep[how_many - 1])]], axis=1)
		how_many -= 1
	print(list(file.columns))
	return



def get_headers(file1: pd.DataFrame, file2: pd.DataFrame) -> None:
	file1 = drop_columns(file1)
	file2 = drop_columns(file2)
	return
