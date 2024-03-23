# Run this script to carry out the analysis on the dataset.

# example usage:
# make all

all: data/raw/planet-systems.csv data/processed/planet-systems.csv eda results

data/raw/planet-systems.csv : src/read-data.py 
	python src/read-data.py

data/processed/planet-systems.csv: src/clean-data.py data/raw/planet-systems.csv
	python src/clean-data.py

eda : data/processed/planet-systems.csv src/data-eda.py 
	python src/data-eda.py

results : data/processed/planet-systems.csv src/data-results.py 
	python src/data-results.py

clean_data:
	rm -f data/processed/planet-systems.csv
	rm -f data/raw/*

clean_results:
	rm -f results/tables/logistic_regression_df.csv
	rm -f results/tables/random_forest_classifier_df.csv
	rm -f results/tables/accuracy.csv
	rm -f results/tables/confusion_matrix.csv
	rm -f results/figures/confusion_matrix.png

clean_eda:
	rm -f results/figures/star_count_hist.png
	rm -f results/figures/sy_umag.csv
	rm -f results/figures/sy_gmag.csv
	rm -f results/figures/sy_rmag.csv
	rm -f results/figures/sy_imag.csv
	rm -f results/figures/sy_zmag.csv
	rm -f results/figures/sy_umag.png
	rm -f results/figures/sy_gmag.png
	rm -f results/figures/sy_rmag.png
	rm -f results/figures/sy_imag.png
	rm -f results/figures/sy_zmag.png

clean: clean_data clean_results clean_eda

clean_all: clean
