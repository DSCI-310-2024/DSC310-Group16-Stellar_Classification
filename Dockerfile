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

# install make and PDF viewer
RUN apt-get update && apt-get install -y make evince

# install quarto
ENV QUARTO_VERSION="1.4.545"

RUN curl -o quarto-linux-amd64.deb -L https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb
RUN apt-get install gdebi-core -y
RUN gdebi quarto-linux-amd64.deb --non-interactive
# install TeX for quarto
RUN quarto install tinytex
=======
# install a PDF viewer and make
RUN apt-get update && \
    apt-get install -y \
        make \
        evince

# carry out the analysis
RUN make all

# open the PDF file with the PDF viewer
CMD ["evince", "reports/Spectral_type_classification_report.pdf"]
