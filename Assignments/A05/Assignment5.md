# Bio5488 SP2025: Assignment 5

### Gene Expression

**Due Date:** Friday, 2/21, 11:59 PM  
**Last Modified:** 2/11/2025

---
## Overview
The goal of this assignment is to compare RNA-seq data for 20 subjects at risk of developing type 2 diabetes before and after one year of an exercise intervention. You will analyze alterations to gene expression in muscle biopsy samples. 

---
## Reminders & Start Guide

**Always** remember to use an interactive job to run command-line tools (like python, bowtie2, bedtools) on the RIS. Onc eyou submit an interactive job, you must activate your conda enrivonment to use tools and dependencies within the docker image. 
 ```bash
 $ bsub -ls -q -workshop-interactive -G -compute-workshop -a 'docker(takinwe1/bio5488:0.0)' /bin/bash 
 $ conda activate bio5488
```

 If the command line returns a CondaError when you attempt to activate the conda environment, you can hardcode the path to the tool. Ex:
 ```bash
/opt/conda/envs/bio5488/bin/python3
/opt/conda/envs/bio5488/bin/bowtie-2
/opt/conda/envs/bio5488/bin/bedtools
```

 Set the path to the class Assignments directory:
```bash
classDir=/storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments
```
View the contents:
```bash
$ ls -vlh ${classDir}
$ ls -vlh ${classDir}/*
```
Navigate to your working directory:
 ```bash
$ cd ${classDir}/A05/Users/<WUSTLKEY>
 ```



 ## Instructions
 Copy the incomplete scripts from the Assignment folder to your work directory.
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
There are prompts in `gene_expression.py` where the code needs to be edited by you (look for TODOs and comments in the script).
The data is stored in a series of dictionaries as you filter and normalize. The keys of these dictionaries are gene names. The value associated with each key (in this case gene) will be a list containing the expression levels of theat gene found in each samople in your study. 

Open up `gene_expression.py` and **read through first** to get a sense of what you will need to do. 

### Part 0: Functions
- In the doc string of `gene_expression.py` write a general discription of what the script does.
- Make the script exit if the wrong number of input parameters are used.

Read the `counts_per_million` and `library_sizes` functions to understand what they do. Then:
 - Fill in the code for the `translate_dictionary` function, This function will translate your data from having one key per gene to one key per sample. In the translated dictionary, the value assocaited with each key (sample) will be that sample's gene expression levels at each gene.
 - Add comments to the code in the `upper_quartile_norm` function to explain what each line does.
 - Write a function to calculate Fisher's Linear Discriminant (and add comments!) for all genes in your count dictionary. Call your function `fishers_linear_discriminant` Remeber that functions should be able to work with different data sets so make sure that your function is flexible and could work with data with different numbers of before and after samples.

---

### Part 1: Data filtering
You will need to use the functions above to complete `gene_expression.py`
To filter the data, you will need to remove genes that provide little to no information about the amount of gene expression. Therefore, remove genes that have counts in all samples. To do so, create a new dictionary with genes that pass your filter. ** Do not alter the orgiinal data file!!! ** For each filtering step, you should save the newly filtered data in a new dictionary

**Question 1:** How many genes are left after removing genes with zero expression in all samples?

Next, caclculate the counts per million (cpm) for each gene left in your data using the `counts_per_million` function. This function returns a dictionary similar to the raw counts dictionary but with cpm values instead. 
Apply the `counts_per_million` function to your data tthe passed the first filter. Now create a new dictionary of raw counts by including gnes that pass your second filter. The second filter should not let a gene through if 20 or more (>=20) samples have cpm <1. (This should generate a dictionaru with raw counts, not cpm values).

**Question 2:** How many genes are left after removing genes where 20 or more samples have cpm <1? 


---
### Part 2: Data visualization
Plot the library sizes (total counts) for each sample using the raw counts for the genes left after filtering. For full credit, make sure the x-acis, y-acis, and the plot itsellf have information titles. The y-axis should have libary size reported as millions of counts. Save your plot as 'library_size.png`

**Question 3:** What is the range of library sizes (min, max)?

---
 ### Part 3: Data normalization

To normalize your data, use an upper quartile normalization of the raw counts left after filtering. Use the `upper_quartile_norm` function to normalize the data you have left after the filtering steps. Write additional code to redo the total counts plot from Part 2 using the normalized count data. Save your new plot as `library_size_normalized.png` 

**Question 4:** What is the rang eof library sizes after normalization (min, max)?

**Question 5:** Compare the two libary size bar charts you made. How did the distribution of library sizes change after normalization? Briefly discuss why it is important to normalize your RNA-seq data.

---
### Part 4: Data exploration 

Now that the data is filtered and normalized, you are ready to compare the Before and After samples. Use Fisher's Linear Discriminarnt (FLD) to compare the two groups. Calculate FLD for each gene and output the genes with the ten highest FLD values (include the gene name and FLD value). Make sure your comments explain each step. 

Generate a bar graph of the upper quartile normalized mean expression level in each group for the gene you want to follow up on. Include standard error (SEM) bars to give a sense of how variable your data is. Of course, label your x and y axes and title your graph. Save your plot as `mean_expression.png` The standard error of the mean (SEM) of a group is calculated as the standard deviation of the group divided by the square root of the number of samples in the group.   

**Question 6:** 
What are the top ten differentially expressed genes according to your FLD analysis? (Copy and paste your function’s output.) Do these genes make sense given the tissue and groups in the experiment?    
**Question 7:** 
Does your result point toward one gene with large effect or many genes with small effects? Does RNA-seq expression data always give researchers a clear answer?    
**Question 8:**
How does the study design of this experiment relate to the assumptions made when studying gene expression data?   
**Question 9:**
If you were going to spend time and money following up on one of these top ten genes, what would be your candidate and why? (There could be many correct answers.)    

---

### Extra Credit

Calculate the Euclidean distance matrix for your samples using the normalized data and/or plot a dendrogram showing the relationship between samples, labeling each leaf with the appropriate sample name. Save your dendrogram as `dendrogram.png`

**EC Question 1** 
What do you expect to see? 

**EC Question 2**
What did uyou actually see? If you did not find what you expected, what sorts of variation could account for this? 

---

## What to turn in
- Edited script: `gene_expression.py`
- Output files
    - `library_size.png`
    - `library_size_normalized.png`
    - `mean_expression.png1
- Your completed `README.txt`
- Extra credit: `dendrogram.png`
