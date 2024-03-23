# Use the specified Jupyter notebook image as the base
FROM continuumio/anaconda3

# Install packages from conda forge channel
RUN conda install -c conda-forge -y\
    python=3.11 \
    scikit-learn=1.2.2 \
    matplotlib==3.8.3 \
    pandas=2.2.0 \
    pyarrow=15.0.1 \
    jupyterlab=4.0.13 \
    click=8.1.7

# create the directory /home/dsci
RUN mkdir -p /home/dsci

# set the working directory to /home/dsci
WORKDIR /home/dsci

# clone the project into the current directory
RUN git clone https://github.com/DSCI-310-2024/DSCI310-Group16-Stellar_Classification.git

# switch to the project directory
WORKDIR /home/dsci/DSCI310-Group16-Stellar_Classification

# install a PDF viewer and make
RUN apt-get update && \
    apt-get install -y \
        make \
        evince

# carry out the analysis
RUN make all

# open the PDF file with the PDF viewer
CMD ["evince", "reports/Spectral_type_classification_report.pdf"]
