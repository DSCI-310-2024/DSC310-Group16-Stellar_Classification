# Use the specified Jupyter R-notebook image as the base
FROM continuumio/anaconda3

# Install packages
RUN conda install --yes \
    'python=3.12' \
    'jupyterlab=4.1.2' \
    'scikit-learn=1.4.1' \
    'matplotlib=3.8.3' \
    'pandas=2.2.0' \
    'pyarrow=15.0.0'