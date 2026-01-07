# Bio5488 SP2026: Assignment 1

### Counting Nucleotides and Determining if a Sequence is i.i.d.

**Due Date:** Friday, 1/23, 11:59 PM  
**Last Modified:** 1/7/2026

---

## Overview
The goal of this assignment is to gain experience handling genomic sequences by using simple scripts to test the hypothesis that genomic sequences are "i.i.d." (independent and identically distributed). You will analyze sequences from human chromosome 22, calculate nucleotide frequencies, and compare them with a first-order random background model.

---

## Quick Start Guide

### Connect to the Secure Network
1. Connect to the `wustl_secure` Wi-Fi network or use a VPN via the Cisco Secure Client. Refer to the [Connecting to WashU Resources guide](#).

### SSH into the RIS Compute Platform
Run the following command in your terminal:
```bash
$ ssh <WUSTLKEY>@compute1-client-1.ris.wustl.edu
```
Replace `<WUSTLKEY>` with your WUSTL username. After logging in, your prompt should resemble:
```bash
[<WUSTLKEY>@compute1-client-1 ~]$
```

### Assignments Directory
Set the path to the class Assignments directory:
```bash
classDir=/storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments
```
View the contents:
```bash
$ ls -vlh ${classDir}
$ ls -vlh ${classDir}/*
```

---

## Instructions

### Part 1: Obtain Human Chromosome 22 Sequence
1. Navigate to your working directory:
   ```bash
   $ cd ${classDir}/A01/Users/<WUSTLKEY>
   ```
2. Download the sequence file:
   ```bash
   $ wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.39_GRCh38.p13/GCF_000001405.39_GRCh38.p13_assembly_structure/Primary_Assembly/assembled_chromosomes/FASTA/chr22.fna.gz
   ```
3. Decompress the file:
   ```bash
   $ gunzip chr22.fna.gz
   ```
4. View the first 10 lines:
   ```bash
   $ head chr22.fna
   ```
5. Copy the `README.txt` template:
   ```bash
   $ cp ${classDir}/A01/Assignment_Data/README.txt .
   ```

### Part 2: Analyze Nucleotide Counts
1. Copy the `nuc_count.py` script:
   ```bash
   $ cp ${classDir}/A01/Assignment_Data/nuc_count.py .
   ```
2. Run the script on `chr22.fna`:
   ```bash
   $ bsub -Is -q workshop-interactive -G compute-workshop -a 'docker(takinwe1/bio5488:0.0)' python3 nuc_count.py chr22.fna
   ```
3. Record the nucleotide counts.

### Part 3: Modify `nuc_count.py`
Update the script to also calculate and output nucleotide frequencies, excluding `N` and other non-ACGT characters.

### Part 4: Random Sequence Generation
1. Copy the `make_seq.py` script:
   ```bash
   $ cp ${classDir}/A01/Assignment_Data/make_seq.py .
   ```
2. Complete the script.
3. Generate a random sequence of length 1,000,000 using frequencies from Part 3:
   ```bash
   $ bsub -Is -q workshop-interactive -G compute-workshop -a 'docker(takinwe1/bio5488:0.0)' python3 make_seq.py 1000000 0.25 0.25 0.25 0.25 > random_seq_1M.txt
   ```

### Part 5: Dinucleotide Frequencies
1. Modify `nuc_count.py` to calculate dinucleotide frequencies using an overlapping window.
2. Run the script for `chr22.fna` and `random_seq_1M.txt`. Compare the results and provide a biological explanation for differences.

---

## Submission
Submit the following files to your submission folder:
```bash
$ subDir=${classDir}/A01/Submissions/Users/<WUSTLKEY>
```

1. Modified `nuc_count.py`
2. Completed `make_seq.py`
3. `random_seq_1M.txt`
4. `README.txt`

Copy files to the submission directory:
```bash
$ cp <file_name> ${subDir}
```

---

## Questions to Address in `README.txt`
1. **How to run `nuc_count.py`.**
2. **How to run `make_seq.py` for length 1,000,000 with calculated frequencies.**
3. **Nucleotide counts of `chr22.fna`.**
4. **Nucleotide frequencies of `chr22.fna`.**
5. **Dinucleotide frequencies of `chr22.fna` and `random_seq_1M.txt`.**
6. **Biological explanation for differences between dinucleotide frequencies.**

---

## Comments and Suggestions
- **Comments:** Note anything that went wrong or was unclear.
- **Suggestions:** List programming or genomics topics that could have made this assignment smoother.

---

**Resources:**
- [RIS Compute Quick Start Guide](#)
- [Connecting to WashU Resources Guide](#)
