# LDproxy-batch-query
Performing a batch query to retrieve SNPs in linkage disequilibrium with a list of variants from a genome wide association study for schizophrenia.

# Background

  Genome wide association studies identify genetic variants that are correlated with a specific trait or disease. These variants are usually single nucleotide polymorphisms (SNPs) which are locations on the genome that may have one of two possible alleles with a minor allele frequency of greater than 5%. [This](https://www.nature.com/articles/s41586-022-04434-5) particular study  identified ~300 variants that are statistically correlated with schizophrenia. 

  Variants often occur dependently of each other. Linkage disequilibirum (LD) occurs when genetic variants are statistically likely to be present together due to being in close enough physical approximation that they are inherited in a block and are not separated in the process of recombination or "crossing over."

  Because of LD and because only a select group of SNPs are genotyped for GWAS, it is worthwile to also examine variants that are correlated with the identified variants of the study. This is achievable thanks to tools like [LDproxy](https://ldlink.nih.gov/ldproxy?ref=53731) which retrieve proxy variants given an rsID (Reference SNP cluster ID). 

# Project Description

  This project aims to conduct a batch query to retrieve associated variants with $R^2 ≥ .01$ by using an R to access the LDLink API, then parsing the resulting data to remove variants that do not meet the threshold. 
