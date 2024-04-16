# start from the Jupyter scipy-notebook as a base
FROM quay.io/jupyter/scipy-notebook:2024-02-24

USER root

# install packages python and quarto from conda forge channel
RUN conda install -c conda-forge -y python=3.11 \
    quarto=1.4.550

# install dependencies
RUN pip install classifyspectraltype==0.2.0 \
    pyarrow==15.0.1 \
    click==8.1.7 \
    tabulate==0.9.0

# create the directory /home/dsci
RUN mkdir -p /home/dsci

# set the working directory to /home/dsci
WORKDIR /home/dsci

# clone the project into the current directory
RUN git clone https://github.com/DSCI-310-2024/DSCI310-Group16-Stellar_Classification.git

# switch to the project directory
WORKDIR /home/dsci/DSCI310-Group16-Stellar_Classification

# install make 
RUN apt-get update && apt-get install -y make lmodern
