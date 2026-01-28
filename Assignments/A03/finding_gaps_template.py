#!/usr/bin/env python3
'''
Usage: python3 nuc_count.py <fastafile>

fastafile = file containing a fasta format sequence from a single chromosome. 
'''

# Import modules
import os
import sys
import math
import matplotlib.pyplot as plt


# Check that the right number of command line arguments was given. If not, print the documentation and exit.
if len(sys.argv) != 2:
    sys.exit(__doc__)

#save the input arguments as variables
file_path = sys.argv[1]
basename = os.path.splitext(os.path.basename(sys.argv[1]))[0]

# open the file and store the header
fasta = open(file_path)
header = fasta.readline()

# initialize a string
sequence = ""

# loop over the fasta file to read in the sequence
for line in fasta:
    nucleotides = line.strip().upper()
    sequence = sequence + nucleotides
fasta.close()

#create a nucleotide and dinucleotide dictionary for tracking counts of each dinucleotide and nucleotide
ACTG="ACTG"
nuc_dict={}
dinuc_dict={}
for i in range(0, len(ACTG)):
    nuc_dict[ACTG[i]] = 0
    for j in range(0,len(ACTG)):
        dinuc_dict[ACTG[i]+ACTG[j]]=0


#Part 1.1
### TODO: count and print the nucleotide frequencies (feel free to re-use your code from prior assignments) (exclude Ns)

#Part 1.2
### TODO: print the size of chromosome 22 (include Ns here)

#Part 1.3
### TODO: count and print the frequencies for each dinucleotide in alphabetical order (exclude Ns here)

#Part 1.5
###TODO: find the number of gaps in the chromosome assembly (hint: track Ns)
### TODO: print out the length of each gap in the chromosome assembly
#Part 1.5
#TODO: Plot the log (base 10) of gap lengths on a histogram 
