

## Assignment 2: Sequence technology

**Due date: Friday, 1/30 11:59pm**

Bio5488, Spring 2026 Last modified 01/07/26

You are provided with sequencing reads from an enrichment sequencing experiment.

Map the reads back to chr22 and identify what is enriched.

Work in your working directory: ``` /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Users/<username>/ ```

When you're done, copy over your final files to the submissions directory: ```/storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Submissions/Users/<username>/ ```

**Don't forget your readme file!**

**1. Copy files to your working directory.**
   
```bash
cp \
  /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Assignment_Data \
  /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Users/<username>/ 
```
   Four files in total (chr22.fa, reads.fq, nuc_count_FINAL.py, README.txt) should be in the folder.
   
**2. Modify the .bashrc file to initialize the conda environment.**
   
Here, we're showing how to do this in a command-line based text editor named vim. You can use any text editor you want, though!

```bash
cd ~ # go to your the home folder
vim .bashrc
```

There will be a section titled as:

```bash
# User specific aliases and functions
```

Type "i" to enter insert mode, so you can edit the file.
If you wonder why you type "i", you can look at this short tutorial: https://eastmanreference.com/a-quick-start-guide-for-beginners-to-the-vim-text-editor

Note: you can do very fancy things with vim, but simple commands are already very useful.

Copy the following code below this section:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/conda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/conda/etc/profile.d/conda.sh" ]; then
        . "/opt/conda/etc/profile.d/conda.sh"
    else
        export PATH="/opt/conda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

save and exit.

First, press "Escape" ("ESC" key on the keyboard) to escape insert mode.
In vim, :w means write (i.e. save), and :q means quit.

We can combine these in a single command.
```
:wq
```
*Then log out of RIS and back in.*

**3. Specify the working path for the Docker container**
   
```bash
$ export LSF_DOCKER_VOLUMES='/storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Users/<username>:/storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Users/<username>'
```

**4. Create the Docker container**

You can only submit bsub jobs from you home directory!
```bash
bsub -Is -q workshop-interactive -G compute-workshop -a 'docker(takinwe1/bio5488:0.0)' /bin/bash
```

**5.  Activate conda environment and enter your working directory**

```bash
conda activate bio5488
cd /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A02/Users/<username>/
```
If this returns a CondaError, you can code the path to the tools each time you use it. Ex:
```bash
 /opt/conda/envs/bio5488/bin/python3
 /opt/conda/envs/bio5488/bin/bowtie-2
 /opt/conda/envs/bio5488/bin/bedtools
```

Now you are ready for sequence alignment!

**Task1: Build a index for chr22**

Genome indexing aims to store the context of the genome to make the searching task more efficient. Using Bowtie2, build an index for chr22. The index building function is based on bowtie2-build:
```bash
$ bowtie2-build <path to chr22.fa> <index filename prefix (minus trailing .X.bt2):eg. chr22_idx>
```

bowtie2-build will create various files under the name specified with different file extensions. To learn about the various options available in bowtie to map sequencing reads, enter:
```bash
$ bowtie2 -h
```
**Task2: Align the reads to chr22**

Once you've built the index for chr22, align the reads to chr22 and create an output file for the standard output, and create a report file by piping the bowtie2 summary to a new text file, (i.e, saving the output using the 2> to a text file):

```bash
$ bowtie2 <write your options here. Note that the reads in reads.fq are unpaired> 2>  <report_file.txt>
```

### Requirements
* Your alignment output file should be saved in a SAM (sequence alignment format) format.
* The report file should contain the alignment summary.
* The alignment summary is printed to the standard error stream.

The bowtie 2 manual talks about this in more detail.

The expected out put summary looks like:
```
20000 reads; of these:
20000 (100.00%) were unpaired; of these:
1247 (6.24%) aligned 0 times
18739 (93.69%) aligned exactly 1 time
14 (0.07%) aligned >1 times
93.77% overall alignment rate
```
#### Question 1:
Report the command you used to align the reads.

How many reads map uniquely to chr22?

How many reads map to multiple locations?

How many reads were unmappable?

Task3: Align the reads to chr22

Using the script “nuc_count_FINAL.py”, identify the frequency of each nucleotide and di-nucleotide. What is enriched in this dataset? (Hint: Look at the relative enrichment of single and dinucleotides)

#### Question 2:

Report the enrichment of all single and di-nucleotides. Enrichment should be calculated as a fold change against an expected background calculated using previously measured values.

Describe how you calculated the enrichment. Mention what the dataset is enriched for and interpret it. What assay(e.g., RNA-seq, CHIP-seq, WGBS..) do you think these data came from given what sequences these assays themselves enrich for?

What to turn in:
* Output files
* Alignment file 
* Report file
* Your README.txt with the answers to the questions and the commands you used to answer the questions.

-------------------------------------

README.txt Template: 

#### Question 1

{Your command with specific file names}

{Number of uniquely mapped reads}

{Number of multi mapped reads}

{Number of unmapped reads}

#### Question 2

{What is enriched in this dataset}

{Single nucleotide enrichment scores}

{Dinucleotide enrichment scores}

{Description of how enrichment scores were calculated}

{Assay,  Explanation}

#### Comments:

{Things that went wrong or you cannot figure out}

#### Suggestions:

{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}

---------------------------------------
                                            
