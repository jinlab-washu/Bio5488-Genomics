

## Assignment 3: Sequence technology

**Due date: Friday, 02/07 11:59pm**

Bio5488, Spring 2025 Last modified 01/25/25

**Face Off: hg38 versus CHM13.**

20 years after the draft human reference genome was released, we are now using a 
very high-quality genome assembly that we call hg38. But hg38 has several limitations 
(which we discussed in class). One limitation is, it is still not 100% complete, having a 
number of gaps and missing pieces. The telomere-to-telomere (T2T) consortium 
recently released a complete human genome assembly that we call CHM13. Let’s take 
a closer look at the differences between hg38 and CHM13. For your convenience, chr22 
sequences from hg38 and CHM13 are provided here: 

```bash
AssignmentDir="/storage1/fs1/workshops/Active/BIO5488/SP2025.L41.BIOL.5488.01/Assignments/A03"
hg38="${AssignmentDir}/Assignment_Data/hg38-chr22.fa"
CHM13="${AssignmentDir}/Assignment_Data/t2t-chr22.fa"
```
Copy these files to your assignment3 working directory.

If you need a refreshment of how to navigate to your working directory, please refer Assignment2.

---

### Part 1. Characterize the differences between hg38 and CHM13.
Copy the incomplete script `finding_gaps.py` from the ```$AssignmentDir``` folder to your assignment3 working directory. There are prompts in `finding_gaps.py` where you need to work. Please look for comments and 
TODOs in the script that will tell you what you need to do. Once you have completed this 
script it should be able to parse through each of the above reference files for 
chromosome 22 and provide the following information: 
    1) Size of the chromosome (include Ns for this)
    2) Frequency of A, C, G, T. (ignore Ns for this)
    3) Frequency of di-nucleotides. (ignore Ns for this)
    4) How many gaps are there in hg38? How many in CHM13? Please submit and
 plot gap size distribution in hg38: y-axis: number; x-axis: size. Hint: just count
 stretches of Ns.
 Please be sure to name the output plot **hg38-chr22_gap_distribution.png**

**Small Extra credit opportunity**: 
In addition to the standard histogram, display the distribution in a more visually pleasant 
manner using your `finding_gaps.py` script. 
The following questions associated with part 1 should be answered in your 
README.txt. Please also add the command used to run the script to your README.txt. 

**Question 1)** 

What is the size of the chromosome from each assembly? 

**Question 2)**

How does the distribution of nucleotide and dinucleotide frequencies in CHM13 
compare to that of hg38? What might be an explanation for the differences, or the lack 
of differences observed? 

**Question 3)**  

How many gaps are there in hg38 and CHM13? 

---

### Part 2. Map a functional genomics dataset of human trophoblast (ATAC-seq).
ATAC-seq data: 
```bash
${AssignmentDir}/Assignment_Data/test-500k.fq 
 ```
Once again please copy the above file to *your assignment3 working directory* where you may then use it. We will continue our practice with bowtie2. You will need to construct an index file for the hg38-chr22 reference and the CHM13 chr22 reference. 

```bash
bowtie2-build <path to hg38-chr22.fa> <index filename prefix (minus trailing .X.bt2) eg. hg38-chr22_idx>  
bowtie2-build <path to t2t-chr22.fa> <index filename prefix (minus trailing .X.bt2) eg. t2t-chr22_idx>  
```
Once you have built the index files, use bowtie2 to map the reads to hg38 and CHM13, and compare mapping result differences.  

```bash
bowtie2 <write your options here. Note that the reads in test-500k.fq are unpaired> 2> <report file>
```

**Question 4** 

What is the number of mappable reads, non-mappable reads, uniquely-mapped reads, 
for both hg38 and CHM13? Explain any similarities/differences you observe between 
the two. 

**Question 5** 

What is the percent of unique reads out of total mappable reads as well as the percent 
of multi-mapped out of total mappable reads for both hg38 and CHM13? Provide an 
explanation for any differences you observe in either rate between the two assemblies. 
A common step during the processing of data prior to analysis is the removal of 
duplicate reads present in the output sam file. Samtools is a suite of tools that allows us 
to evaluate and remove these duplicates. 

Samtools is already installed on the server. To see the tools available when using 
samtools enter  
```bash
samtools  
```
To learn about the options available for each tool use  
```
samtools <write the tool name you are interested in here> 
```
To mark and remove duplicates 4 tools must be used on the sam files that are output 
from bowtie2. Here you will use the samtools `collate`, `fixmate`, `sort`, and `markdup` tools 
(in that order) to do so. 
More information on the different tools is available here: 
http://www.htslib.org/doc/samtools.html 
Hint: It is recommended to follow the guide at the bottom of 
http://www.htslib.org/doc/samtools-markdup.html, though you will need to add a few 
additional flags to answer the following question. 

**Question 6** 

What is the fraction of de-duplicated reads in total mappable reads? and compare 
between hg38 and CHM13. 

**Extra Credit opportunity**: 
Write a python script that parses through a bowtie2 aligned sam file and tallies the 
number of duplicate reads.

---

### Part 3. BLAST OFF! 
For part 3 we will be exploring the commonly used tool BLAST that is hosted by NCBI. 
Go to http://www.yeastgenome.org/ Search for the gene Rap1. Get the nucleotide 
sequence for the Rap1 coding region, and go to http://www.ncbi.nlm.nih.gov/. Find 
**BLAST**. Choose translated query vs. protein database (**BLASTX**). BLASTX will 
translate the sequence into a peptide and blast it against a protein database.  
Paste the Rap1 sequence in the space provided (in FASTA format) and select the "nr" 
database. 
Click on **BLAST** to submit the job. How much time does it take to finish the job? 
When you get the output, answer these questions: 

**Question 7**  
Why did you want to use the "nr" database as opposed to any of the other database 
options? 

**Question 8**

How many hits did you get with an **e-value < 1**? (Hint: Change Algorithm parameters to 
customize output – set Max target sequences to 250)

**Question 9** 

What non-Saccharomyces species has the best hit? In that species, what is the score 
and % identity for Rap1's closest relative?  
Next, run BLASTX with the BLOSUM80 scoring matrix instead of the default 
BLOSUM62 matrix. (The scoring matrix parameter can be changed by clicking on the 
Algorithm parameters links.)  

**Question 10** 

Did you get more or fewer hits (with e-value < 1) than before? Why? 

**Question 11** 

Now, using BLOSUM80, what species is the closest non-Saccharomyces relative? 

**Question 12**  

Find the protein that was the closest relative according to BLOSUM62 (from Question 
3). What is the new % identity and score for that protein when using BLOSUM80?  
Now, BLAST again with BLOSUM62, but lower the Gap Existence penalty to 7. (Hint: 
Click on Algorithm Parameters and find Gap Costs under Scoring Parameters.)  

**Question 13** 

How many hits did you get with **e-value < 1**? Why do you think this number changed the 
way it did?  

**Question 14** 

Why did the score of the closest ortholog change the way it did? 

**Question 15** 

If you lowered the word length, would you expect the search to take more or less time? 
Why?  

**Question 16** 

Isn't online BLAST really slow? Hopefully, you have now realized two things. First, when we say "closest relative," the  answer really depends on the scoring matrix and parameters we use. Second, using BLAST online is really slow. 

#### What goes in your submission directory? 
(1) Your README.txt with the answers to the questions and the commands you used to answer the questions.

(2) finding_gaps.py script

(3) hg38-chr22_gap_distribution.png

(4) Bowtie2 Alignment files

(5) Bowtie2 Report files

(6) Samtools duplicates removed sam file

Extra credit files:

(E1) Additional gap size distribution plot.

(E2) Python script for tallying duplicates from the bowtie2 aligned sam file.

