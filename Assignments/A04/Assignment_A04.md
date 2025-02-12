# Bio5488 SP2025: Assignment 4


## Assignment 4: Integrative epigenomics analysis

**Due date**: Friday, 2/14 11:59pm

**Last Modified:**  01/28/25

---

## Overview
The goal of this assignment is to gain experience handling mapping genomic regions with bedtools and investigating epigenomic data. You will analyze methylation levels in human chromosome 21 from a brain sample, compare methylation levels at different functional genomic locations, and map histone mark ChIP-seq data.

---
## Introduction 

CpG islands (CGIs) are important regulatory regions in the genome. What are their epigenetic
profiles? Let’s find out! 

We obtained several epigenomic datasets from the Roadmap Epigenome Project from a human brain germinal matrix sample:
* BGM_WGBS.bed : methylation data

There are also accompanying annotation files:
* CGI.bed: locations of CGIs
* CpG.bed: locations of CpGs
* refGene.bed: locations of RegSeq genes

File descriptions can be found at the end of this markdown file. These files are based on the hg19 reference genome assmebly, and have been simplified to just focus on chr 21. Full datasets can be found in the Roadmap Epigenome Project Portal (https://egg2.wustl.edu/roadmap/web_portal/index.html)

All files can be found in 
```bash
/storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Assignment_Data/
```
Copy them to your home directory. 

```bash
$ cp \
  /storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Assignment_Data/* \
  /storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Users/<username>/
```
**Notes**
* All plots must have informative **axis labels, titles, etc.** 
* We will utilize bedtools to do this analysis, which is already installed on the server. To print the help menu:
```bash
$ bedtools --help
```
* In this asssignment, you will be wiritng scripts that produce output files. Make sure you do not overwrite the output file--do not hardcode the output filename. Instead, you can use Python to dynamically name the output file names based on the input file names. For example:

```python
import
os 
basename = os.path.splitext(os.path.basename(<input_filename>))[0]
plotname = basename + "_methylation_distribution.png"
```

--- 
## Part 1: Analyzing DNA methylation data
### 1.A 
Write a script called "analyze_WGBS_methylation.py that takes a WGBS bed file and:
  1. Calculates the methylation level for each CpG using the formula: 
  $ \text {CpG methylation level} = \frac {\#\text{ C bases}}{\#\text{ C base calls} + \#\text{ T base calls}} $


  2. Writes a file of CpG methylation with 4 columns, name it \<WGBS_bed_basename>_CpG_methylation.bed Do not output CpG islands with 0X coverage.  
    1. Column 1: chromosome  
    2. Column 2: start coordinate  
    3. Column 3: stop coordinate  
    4. Column 4: methylation level  

  3. Plots the distribution of CpG methylation levels using a histogram. SSave this file as <span style='color: red;'>\<WGBS_bed_basename></span><span style='color: blue;'>_CpG_methylation_distribution.png</span>

  4. Plots the distribution of all CpGs for coverages from 0X to 100X as <span style= 'color: red; '> \<WGBS_bed_basename></span><span style='color: blue;'>_CpG_coverage_distribution.png</span >
  5. Calculates and prints the fraction of CpGs with 0X coverage.
  
  The usage of the script will be: 
  ```bash 
  $ python3 analyze_WGBS_methylation.py <WGS bed>
  ```
Run analyze_WGBS_methylation.py on the given WGBS data and paste the command in your README. Copy your output files to your submission directory. 

--- 
#### 1.A Questions
1. What does DNA methylation look like across chromosome 21?
2. What does the CpG coverage look like across chromosome 21?
  1. What fraction of the CpGs have 0X coverage?

--- 
### 1.B
Using bedtools, create a bedfile with the average CpG methylation level in each CGI. This file should be in bedformat. Name your final file with the average CpG methylation level in each CGI <span style= 'color: red; '>WGBS_CGI_methylation.bed.</span >

Paste the commands you used to generate this file in your README.

Hint: use the `bedtools intersect` and `bedtools groupby` subcommands.

### 1.C
Write a script called `analyze_CGI_methylation.py` that takes the average CGI methylation bed file and plots the distrbution of average CGI methylation levels. Save the plot as <span style= 'color: red; '> \<average
CGI methylation bed basename> </span> <span style= 'color: lightblue; '> _distribution.png.

The usage of the script will be:
```bash
$ python3 analyze-CGI_methylation.py <average CGI methylation bed>
```

Run `analyze_CGI_methylation.py` on `WGBS_CGI_methylation.bed`. Save the output figure as `WGBS_CGI_methylation_distribution.png`. Paste the command in your README. 

----


#### 1.C Questions
**Question 3**

What does DNA methylation look like for CpGs in CGIs? How does it compare to all the CpGs on chromosome 21?

----
## Part 2: Identify methylation in promoters and non-promoters
We want to explore the CpG methylation profiles in promoter CGIs versus non-promoter CGIs.

### 2.A 
Write a script called `generate_promoters.py` that uses a bed file of gene coordinates and creates a bed file of their corresponding promoters. The columns will be:
 1. Column 1: chromosome
 2. Column 2: start coordinate
 3. Column 3: stop coordinate
 4. Column 4: gene name
 5. Column 5: strand

 The usage of the script will be:
 ```bash
 $ python3 generate_promoters.py <bed of gene coordinates>
 ```

 Run `generate_promoter.py` on `refGene.bed.` Save the output file as `refGene_promoters.bed` 

 In your README, justify how you defined promoter and paste your command for creating theis file.

 ---

 ### 2.B

 Generate a bedfile of promoters-CGIs called promoter_CGI.bed and a bef file of non-promoter-CHIs called non_promoter_CGI.bed. Promoter-CGIs are defined as CGIs that overlap with a promoter. \(Hint: use `bedtools intersect`)

 In your README, justify your overlapping criteria and paste your commands for creating these files 

 ---

 ### 2.C 

 Calculate the average CpG methylation level for each promoter-CGI and non-promoter-CGI. You will need to use bedtools intersect again. Save these files as `average_promoter_CGI_methylation.bed` and `average_non_promoter-CGI_methylation.bed` \(Hint: see your commands for part 1.A)

 Paste your commands for creating these files in your README. 

 **Question 4**

 How do the DNA methylation profiles of promoter-CGIs and non-promoter-CGIs differ?

--- 

 ### 2.D 
 Use this modified nucleotide count script to calculate the frequences of CpGs in promoter-CGI and non-promoter-CGIs fastas. 
 ```bash
 /storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Assignment_Data/nuc_count_multisequence_fasta.py
 ``` 
Use this chromosome 21 fasta file: 
 ```bash
 /storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Assignment_Data/hg19_chr21.fa
 ``` 

 In your README, paste the CpG frequency for both the promoter-CGIs and non-promoter-CGIs and your commands to calculate the frequences. \(Hint: use `bedtools getfasta` to convert a bedfile to a fasta file.)

 **Question 5**
 
 What is a possible biological explanation for the difference in CpG frequencies? Interpret your results from parts 1.3.0 and 1.3.1: what are the “simple rules” for describing regulation by DNA methylation in promoters?

 --- 

## Extra Credit: Analyze H3K4me3 in promoters and non-promoters

Use the H3K4me3 ChIP-seq data set located here

``` bash 
 /storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Assignment_Data/BGM_H3K4me3.bed

 ```
Use `bed_reads_RPKM.p1` to calculate the ChIP-seq RPKM score for promoter-CGIs and nonpromoter-CGIs using the H3K4me3 ChIP-seq data. Save the output files as `H3K4me3_RPKM_promoter_CGI.bed` and `H3K4me3_RPKM_non_promoter_CGI.bed`.

Past the commands in your README.

Write a script called `analyze_h3K4me_scores.py` that creates on figure with a boxplot of the H3K4me3 RPKM scores distribution for promoter-CGIs and a boxplot of the H3K4me3 RPKM score distribution for non-promoter-CGis. Save the plot as <span style= 'color: red; '> \<basename of first bed of RPKM scores> </span> <span style= 'color: lightblue; '> \_and_ <span style= 'color: red; '> \<basename of secondbed of RPKM scores> </span> <span style= 'color: lightblue; '> .png

The usage of the script will be: 
```bash
$ python3 analyze_h3k4me3_scores.py <first bef of RPKM scores> <second bed of RPKM scores>

```

Run `analyze_H3k4me3_scores.py` on `H3K4me3_RPKM_promoter_CGI.bed` and `H3K4me3_RPKM_non_promoter_CGI.bed`. Save the output figure as `H3K4me3_RPKM_promoter_CGI_and_H3K4me3_RPKM_non_promoter_CGI.png`

Paste your commands in your README

**Extra Credit Questions**

Question 1:  
How does the H3K4me3 signal differ in promoter-CGIs and non-promoter-CGIs?

Question 2: 

What would be a better way to compare H3K4me3 values instead of boxplots? Explain.

--- 
## Submission

Submit the following files to your submission folder:
```bash
$ subDir=/storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A04/Submissions/Users/<WUSTLKEY>
```

 - All scripts you wrote:
    - analyze_WGBS_methylation.py 
    - analyze_CGI_methylation.py
    - generate_promoters.py
 - All output files:
    - BGM_WGBS_CpG_methylation.bed 
    - BGM_WGBS_methylation_distribution.png 
    - BGM_WGBS_CpG_coverage_distribution.png 
    - WGBS_CGI_methylation.bed 
    - WGBS_CGI_methylation_distribution.png 
    - refGene_promoters.bed 
    - promoter_CGI.bed 
    - non_promoter_CGI.bed 
 - Your completed README.txt  
  

**Extra Credit Submission**

- All scripts you wrote:
  - analyze_h3K4me3_scores.py
- All output files
  - H3K4me3_RPKM_promoter_CGI.bed
  - H3K4me3_RPKM_non_promoter_CGI.bed
  - H3K4me3_RPKM_promoter_CGI_and_H3K4me3_RPKM_non_promoter_CGI.png
- Extra credit answers to the README.txt


