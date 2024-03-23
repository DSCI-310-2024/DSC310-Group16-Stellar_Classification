# Run this script to carry out the analysis on the dataset. This file encapsulates
# the whole workflow of project.
# 1) First, the data is downloaded
# 2) It gets processed
# 3) EDA is carried out
# 4) Results are presented
# 5) Final report is rendered

# example usage:
#
# Type in the following lines in your terminal under the root directory of this project:
#
# make clean
#
# make all

all: download preprocess eda results


download: data/raw/planet-systems.csv

data/raw/planet-systems.csv : src/read-data.py 
	python src/read-data.py


preprocess: data/processed/planet-systems.csv

data/processed/planet-systems.csv : src/clean-data.py data/raw/planet-systems.csv
	python src/clean-data.py


eda: results/figures/star_count_hist.png \
	results/figures/sy_umag.csv \
	results/figures/sy_gmag.csv \
	results/figures/sy_rmag.csv \
	results/figures/sy_imag.csv \
	results/figures/sy_zmag.csv \
	results/figures/sy_umag.png \
	results/figures/sy_gmag.png \
	results/figures/sy_rmag.png \
	results/figures/sy_imag.png \
	results/figures/sy_zmag.png

results/figures/star_count_hist.png \
results/figures/sy_umag.csv \
results/figures/sy_gmag.csv \
results/figures/sy_rmag.csv \
results/figures/sy_imag.csv \
results/figures/sy_zmag.csv \
results/figures/sy_umag.png \
results/figures/sy_gmag.png \
results/figures/sy_rmag.png \
results/figures/sy_imag.png \
results/figures/sy_zmag.png : data/processed/planet-systems.csv src/data-eda.py 
	python src/data-eda.py


results: results/tables/logistic_regression_df.csv \
	results/tables/random_forest_classifier_df.csv \
	results/tables/accuracy.csv \
	results/tables/confusion_matrix.csv \
	results/figures/confusion_matrix.png

results/tables/logistic_regression_df.csv \
results/tables/random_forest_classifier_df.csv \
results/tables/accuracy.csv \
results/tables/confusion_matrix.csv \
results/figures/confusion_matrix.png : data/processed/planet-systems.csv src/data-results.py 
	python src/data-results.py


clean_data :
	rm -f data/processed/planet-systems.csv
	rm -f data/raw/*

clean_results :
	rm -f results/tables/logistic_regression_df.csv
	rm -f results/tables/random_forest_classifier_df.csv
	rm -f results/tables/accuracy.csv
	rm -f results/tables/confusion_matrix.csv
	rm -f results/figures/confusion_matrix.png

clean_eda :
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

clean : clean_data clean_results clean_eda clean_reports

clean_all : clean


render: reports/Spectral_type_classification_report.html

reports/Spectral_type_classification_report.html : reports/Spectral_type_classification_report.qmd \
data/processed/planet-systems.csv \
data/raw/* \
results/tables/logistic_regression_df.csv \
results/tables/random_forest_classifier_df.csv \
results/tables/accuracy.csv \
results/tables/confusion_matrix.csv \
results/figures/confusion_matrix.png \
results/figures/star_count_hist.png \
results/figures/sy_umag.csv \
results/figures/sy_gmag.csv \
results/figures/sy_rmag.csv \
results/figures/sy_imag.csv \
results/figures/sy_zmag.csv \
results/figures/sy_umag.png \
results/figures/sy_gmag.png \
results/figures/sy_rmag.png \
results/figures/sy_imag.png \
results/figures/sy_zmag.png 
	quarto render reports/Spectral_type_classification_report.qmd

clean_reports:
	find reports ! -name '*.qmd' -type f -exec rm -f {} +