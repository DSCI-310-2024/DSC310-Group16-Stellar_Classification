# DSCI_310-Group_16

## Project Title: Stellar Classification Predictor

Contributors: Aron Bahram, Olivia Lam, Lucy Liu, and Viet Ngo

## Project Summary 

Our project looks towards the skies to classify stars to their given spectral types according to their different electromagnetic radiation magnitudes. Our goal is to expand our understanding of stars through their five radiation band types, and explore how data analysis can further our knowledge beyond our galaxy through the study of photometry, dynamics of celestial bodies, and stellar interactions. Our research comes from a data set on planetary systems from NASA’s Exoplanet Archive. Our simple categorization of stars may seem small, but it contributes to the bigger pursuit of celestial research and perhaps even planetary exploration.

## Reproducing the results in a docker container

1. Open up a terminal and go to a directory where you want to clone the repository

3. Make sure git, docker, and docker-compose are installed on your system

4. Make sure docker is running on your system

5. Clone the repository from Github into your selected folder:

   `git clone https://github.com/DSCI-310-2024/DSCI310-Group16-Stellar_Classification.git`

6. Change to that directory using the command `cd DSCI310-Group16-Stellar_Classification`

7. Run docker-compose to carry out the analysis in a reproducable way:

   `docker-compose run --rm analysis-env bash -c "make clean && make all"`

8. The generated report will show up under `results/Spectral_type_classification_report.html` in the cloned repository, which you can open up by navigating to it in your file explorer and opening it with your browser by double clicking it. If that doesn't work, try right clicking, and selecting open with... and then select your preferred browser to open it in.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Dependencies

  - `jupyterlab`
  - `scikit-learn`
  - `matplotlib`
  - `click`
  - `pandas`
  - `python`
  - `pyarrow`
  - `tabulate`

Also, see Dockerfile for specific versions.

## License

Our project is licensed under the MIT License and is provided under file: LICENSE
