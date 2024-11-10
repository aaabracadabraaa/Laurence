import pandas as pd
import initialisation

def main() -> None:
	file_names = initialisation.get_filename()
	sea_level: pd.DataFrame = initialisation.read_file(file_names[0])
	sea_anomalies: pd.DataFrame = initialisation.read_file(file_names[1])

	print(sea_level)
	print(sea_anomalies)
	



if __name__ == '__main__':
	main()
