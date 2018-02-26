FROM jupyter/scipy-notebook

RUN conda install --yes \
    'scikit-learn=0.19*' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR
