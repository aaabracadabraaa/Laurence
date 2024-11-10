import pandas as pd

def get_filename():
	file1_name = input("What is the location of sea level data? ")
	if (file1_name == ""):
		file1_name = r"/Users/francois/Desktop/Laurence1/sea-level.csv"

	file2_name = input("What is the location of sea anomalies data? ")
	if (file2_name == ""):
		file2_name = r"/Users/francois/Desktop/Laurence1/temp-anomaly.csv"
	return [file1_name, file2_name]



def read_file(filename: str) -> pd.DataFrame:
	if filename == "":
		print("You didn't enter anything.")
		return None
	try:
		df = pd.read_csv(filename)
		return df
	except FileNotFoundError:
		print(f"Error: {filename} was not found.")
	except pd.errors.EmptyDataError:
		print(f"Error: {filename} is empty.")
	except pd.errors.ParserError:
		print(f"Error: {filename} contains malformed CSV data.")
	except Exception as e:
		print(f"An unexpected error occured: {e}")
	return None

