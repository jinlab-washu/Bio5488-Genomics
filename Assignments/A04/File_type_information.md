# Description of input files
This markdown file describes the data files in assignment4. All coordinates are based on the hg19 reference genome. The data has been reduced to chr 21 for ease.

## Fetal brain sample files:
- BGM_WGBS.bed: contains methylation data from WGBS in bed format. Each row contains the coordinate of a CpG with at least 1X coverage, the number of times the C was sequenced as “C” and the number of times the C was sequenced as “T”. (Note: Reads that mapped to either of the two strands in the CpG were combined.) From these numbers, one can estimate the level of methylation for each CpG, as well as its coverage. The file is in a bed-variant format: 

| Column | Description                                   | Example   |
|--------|-----------------------------------------------|-----------|
| 0      | Chromosome                                    | chr21     |
| 1      | Start coordinate of CpG (0-based, inclusive)  | 9411551   |
| 2      | End coordinate of CpG (0-based, exclusive)    | 9411553   |
| 3      | # of C basecalls for CpG                      | 12        |
| 4      | # of T basecalls for CpG                      | 9         |

- BGM_H3K4me3.bed (for extra credit): contains H3K4me3 ChIP-seq data in bed format. Each row contains the coordinate of a mapped ChIP-seq read, the read, the mapping quality, and the strand the read aligned to: 

| Column | Description                                    | Example                                                             |
|--------|------------------------------------------------|---------------------------------------------------------------------|
| 0      | Chromosome                                     | chr21                                                               |
| 1      | Start coordinate of ChIP-seq read (0-based, inclusive)  | 9411232                                                             |
| 2      | End coordinate of ChIP-seq read (0-based, exclusive)    | 9411382                                                             |
| 3      | Sequence of ChIP-seq read                      | GAGGTAGATCATCTTGGTCCAATCAGACTGAAATGCCTTGAGGCTAGATTTCAGTCTTTGTGGCAGGTGGGGGAA |
| 4      | Mapping quality                                | 25                                                                  |
| 5      | Strand that read mapped to                     | +                                                                   |

## Annotation files:
- CGU.bed: contains locations of CGIs in bed format. Each row contains the coordinate and name of a CGI:  

| Column | Description                                    | Example   |
|--------|------------------------------------------------|-----------|
| 0      | Chromosome                                     | chr21     |
| 1      | Start coordinate of CGI (0-based, inclusive)   | 9437272   |
| 2      | End coordinate of CGI (0-based, exclusive)     | 9439473   |
| 3      | CGI name (derived from the # of CpGs in CGI) (not unique) | CpG: 285  |
| 4      | Number of CpGs in the CGI                      | 285       |

- CpG.bed: contains locations of CpGs in bed format. Each row contains the coordinate of a CpG:  

| Column | Description                                   | Example  |
|--------|-----------------------------------------------|----------|
| 0      | Chromosome                                    | chr21    |
| 1      | Start coordinate of CpG (0-based, inclusive)  | 9411551  |
| 2      | End coordinate of CpG (0-based, exclusive)    | 9411553  |



- refGene.bed: contains locations of refSeq genes in bed format. Each row contains the coordinate of a gene, the gene name, the number of exons in the gene, and the strand of the gene:   


| Column | Description                                    | Example   |
|--------|------------------------------------------------|-----------|
| 0      | Chromosome                                     | chr21     |
| 1      | Start coordinate i.e. leftmost coordinate of gene (0-based, inclusive) | 9825831  |
| 2      | End coordinate i.e. rightmost coordinate of gene (0-based, exclusive)  | 9826011  |
| 3      | Gene name                                      | MIR364    |
| 4      | Number of exons in gene                        | 1         |
| 5      | Strand                                         | +         |
