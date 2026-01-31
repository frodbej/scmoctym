# Binarize gene expression matrices using first quartile threshold

import pandas as pd

datasets = ['pbmc3k', 'foetal', 'pic']
quantile = 0.25

# For each dataset, gene expression values are converted to binary: 1 if expression > Q1, 0 otherwise
for d in datasets:
    input_file = f'gene_expression_{d}.tsv'
    output_file = f'binarized_gene_expression_{d}.tsv'

    gene_expression = pd.read_csv(input_file, delimiter='\t', index_col=0)

    binarized = gene_expression > gene_expression.quantile(quantile, axis=0)
    binarized = binarized.astype('int64')

    binarized.to_csv(output_file, sep='\t')