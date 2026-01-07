# Bio5488 SP2026: Assignment 6

### Gene Expression Week 2

**Due Date:** Friday, 2/27, 11:59 PM  
**Last Modified:** 1/07/2026

---
## Overview
The goal of this assignment is to learn RNA-seq analyis using DESeq2. 

---
## Reminders & Start Guide

**Always** remember to use an interactive job to run command-line tools (like python, bowtie2, bedtools) on the RIS. Once you submit an interactive job, you must activate your conda enrivonment to use tools and dependencies within the docker image. 
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
classDir=/storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments
```
View the contents:
```bash
$ ls -vlh ${classDir}
$ ls -vlh ${classDir}/*
```
Navigate to your working directory:
 ```bash
$ cd ${classDir}/A06/Users/<WUSTLKEY>
 ```


 ## Instructions
 Copy the incomplete scripts from the Assignment folder to your work directory.
All files can be found in 
```bash
/storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A06/Assignment_Data/
```
Copy them to your home directory. 

```bash
$ cp \
  /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A06/Assignment_Data/* \
  /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A06/Users/<username>/
```
### RIS R Studio Setup Instructions ###

1. Access the RIS server via SSH
    - Connect to WUSM network or use the WUSM VPN
    - Use your WUSTL key and login via terminal
    ```bash
    ssh <WUSTL key>@compute1-client-1.ris.wustl.edu
    ```
1. Create an R profile
     - Change into your home directory if not already there. Use ```pwd``` to show current working directory.
     - Create and start editing a new file called ".Rprofile" with your favorite text editor (e.g. vim)
     - Paste the following code in the newly created ".Rprofile" file. 
      ```
      vals <- paste('/storage1/fs1/workshops/Active/BIO5488/R_libraries/',paste(R.version$major,R.version$minor,sep="."),sep="")
      for (devlib in vals) {
          if (!file.exists(devlib))
          dir.create(devlib)
      x <- .libPaths()
      x <- .libPaths(c(devlib,x))
      }
      rm(x,vals)
      ```
1. Access RStudio through the Open OnDemand
   - Login (if necessary) using your WUSTL key to Open OnDemand [here]([url](http://ood.ris.wustl.edu/)
   - Under “Interactive Apps” dropdown menu, select Rstudio. You should see the below screen:
     - ![image](https://github.com/user-attachments/assets/8d1c5739-b72c-485d-b1f1-9c501e22c85d)
   - In the "Mounts" textbox, enter ```/storage1/fs1/workshops/Active/BIO5488:/storage1/fs1/workshops/Active/BIO5488```
   - Under the "Memory" textbox, request 8 GB of memory with the value "8".
   - In the "number of hours", request 8 hours to keep the session running.
   - Other values do not need to be changed.
   - Press 
   - Link to [documentation](https://docs.ris.wustl.edu/doc/compute/compute-ood.html).
