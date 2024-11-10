import initialisation
import clean_up
import merge_data_sets
import toml

import pandas as pd

def get_config():
	with open("config_file.toml", 'r') as fd:
		configs = toml.load(fd)
	return configs


def main() -> None:
	configs: dict = get_config()
	print(configs['file1_loc'])
	file_names = initialisation.get_filename(configs)
	sea_level: pd.DataFrame = initialisation.read_file(file_names[0])
	sea_anomalies: pd.DataFrame = initialisation.read_file(file_names[1])
	print(sea_level, sea_anomalies)

	data_collection = [sea_level, sea_anomalies]
	data_collection = clean_up.clean_up(data_collection[0], data_collection[1], configs)
	data_collection = clean_up.convert_to_datetime(data_collection[0], data_collection[1])
	
	merged_set_limits = merge_data_sets.get_date_limits(data_collection[0], data_collection[1])
	merged_set = merge_data_sets.initialise_merged_data_set(merged_set_limits)
	merged_set = merge_data_sets.fill_merged_set(merged_set, data_collection[0], data_collection[1], merged_set_limits)
	print(merged_set)



if __name__ == '__main__':
	main()
