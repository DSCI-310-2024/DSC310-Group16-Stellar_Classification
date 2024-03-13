# Use the specified Jupyter notebook image as the base
FROM continuumio/anaconda3

# Install packages from conda forge channel
RUN conda install -c conda-forge \
    python=3.11 \
    scikit-learn=1.2.2 \
    matplotlib==3.8.3 \
    pandas=2.2.0 \
    pyarrow=15.0.1 \
    jupyterlab=4.0.13
