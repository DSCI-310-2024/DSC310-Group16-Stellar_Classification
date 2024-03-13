# Use the specified Jupyter notebook image as the base
FROM continuumio/anaconda3


# Install packages
RUN conda install --yes \
    'python' \
    'jupyterlab' \
    'scikit-learn' \
    'matplotlib' \
    'pandas' \
    'pyarrow'