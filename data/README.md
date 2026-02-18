# Data

This directory contains **binarized gene expression data files** used as input by scMOCTYM.

The script `binarize_gene_expression.py` is used to generate the binarized gene expression matrices.

To generate the binarized gene expression matrices, the raw gene expression matrices can be downloaded from the `Data/` folder of [this](https://gitlab.com/andreatangherloni/magneto) repository.

The method also requires the cell cluster assignments associated with each dataset (`cluster_<dataset>.tsv`), which can be downloaded from the same repository.

All the credit for the original datasets and cluster annotations goes to the original authors of that work.
