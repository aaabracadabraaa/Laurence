import pandas as pd
import initialisation
import clean_up
import merge_data_sets

def main() -> None:
	file_names = initialisation.get_filename()
	sea_level: pd.DataFrame = initialisation.read_file(file_names[0])
	sea_anomalies: pd.DataFrame = initialisation.read_file(file_names[1])
	print(sea_level); print(sea_anomalies)

	data_collection = [sea_level, sea_anomalies]
	data_collection = clean_up.clean_up(data_collection[0], data_collection[1])
	data_collection = merge_data_sets.convert_to_datetime(data_collection[0], data_collection[1], 'Day')







if __name__ == '__main__':
	main()
