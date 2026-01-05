>Created by Elle Mehinovic.
>Last modified [01-05-2026](01-05-2026).
# Ris Guide: Navigating BIO5488 Assignments Directories Structure & Workflow Tour

This document explains the directory structure used for weekly assignments and how students should navigate, work on, and submit their files.\. Each directory’s purpose and layout will be explained\, so please follow along via your command line\.

* Since the RIS utilizes a Linux operating system\, users can run basic Linux commands directly on their terminal\. Before we start\, here are some common commands we will be using throughout this tutorial that you may want to get familiar with:
    * <span style="color:#7030A0"> _pwd_ </span> :
      * Prints the current directory you are in
        * <span style="color:#7030A0"> _pwd_ </span>
    * <span style="color:#7030A0"> _cd_ </span> :
      * Allows you to move between directories
        * <span style="color:#7030A0"> _cd_ </span>   <span style="color:#C00000">/path/to/a/directory</span>
    * <span style="color:#7030A0"> _ls_ </span> :
      * Lists files from a current working directory\, or a path given after the command
        * <span style="color:#7030A0"> _ls_ </span>
        * <span style="color:#7030A0"> _ls_ </span>   <span style="color:#C00000">/path/to/a/directory</span>
  > * Note: you will see the command “ <span style="color:#7030A0"> _ls –_ </span>  <span style="color:#7030A0"> _lsh_ </span> ” being used; this just creates a long list\, including size\, in human readable format\. For more information\, please see link below:
  >
  > <p align="center"><a href="https://www.inmotionhosting.com/support/server/linux/ls-command/">LS COMMANDS</a></p>

---
* ### Step 1:
  * Login to the RIS though a ssh via terminal:
    * Please see RIS\_Guide\-How\_To\_Login for more details

  * MacOS Terminal:
  
  <img src="https://github.com/jinlab-washu/Bio5488-Genomics/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating0.png">
  
  * Linux Terminal:
 
  <img width="1000" src="https://github.com/jinlab-washu/Bio5488-Genomics/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating1.png">
  
  * Windows Terminal:
 
  <img src="https://github.com/jinlab-washu/Bio5488-Genomics/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating2.png">


---

* ### Step 2:
  * Once you have logged into the RIS your will see YOUR home directory:
      * You can check your current path\, use the  <span style="color:#7030A0"> _pwd_ </span>  <span style="color:#7030A0"> </span> command:
   
        <img src="https://github.com/jinlab-washu/Bio5488-Genomics/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating3.png">
        
        * Your home directory will always be  <span style="color:#002060">/home/</span>  <span style="color:#A51416"> _\{_ </span>  <span style="color:#C00000"> _WUSTL\_KEY\}_ </span>  <span style="color:#C00000"> </span>
        
---

## The Home Directory

Home Directories
  * What are “Home Directories”?
    * Home directories on RIS are network storage locations where users can store their personal files and settings\, allowing them to access their data from any network\-connected computer\.
  * What should I use my home directory for?
    * Home directories have a lot of limitations\. A user’s home directory should only be used for configuration’s and occasionally mounting and storing very small files by the user\. The primary use of a home directory is for the LSF system and programs which need access to the home directory\.
  * What are the limitations?
    * There are many\, however the main limitations include:  10GB of storage available\, lackluster performance when running jobs \(reading/writing\) and increase risk of caching issues\.
  * Do I have root permissions?
    * No\, even in your home directory\, you will  _NOT_  have root access on the RIS\. Only individuals with granted access from the RIS can run root commands\.
  * What if my program needs to use /home/root?
    * Most programs will allow you to change your home directory\, if it doesn’t do so already\.  If root permissions are 100% needed\, there are ways to work around this via docker build\.

## Assignment Directory Structure

Under each assignment directory (e.g. `A00`, `A01`, …), you will see the following layout:

```text
A00
|-- Assignment_Data
|-- Submissions
|   `-- Users
|       `-- WUSTLKEY
`-- Users
    `-- WUSTLKEY
```

---

## Directory Descriptions

### `Assignment_Data/`
This directory contains the files provided for that week’s assignment (starter scripts, datasets, instructions, etc.).

- **Do NOT edit files in this directory**
- Treat this directory as read-only
- Copy any required files into your personal working directory before making changes

---

### `Users/WUSTLKEY/`
This is **your personal working directory**, named after your WUSTL key.

- Copy files from `Assignment_Data/` into this directory
- Edit code, run commands, and generate results here
- This directory is for active work only

---

### `Submissions/Users/WUSTLKEY/`
This directory is used to **submit your completed work for grading**.

- Copy only finalized files here
- Files in this directory are what instructors will review
- Do not submit intermediate or test files

---

## Example Assignment Layout

Below is an example of what an assignment directory may look like after you have started working:

```text
A00
|-- Assignment_Data
|   |-- COPY_ME_example_assignment.py
|   `-- README.txt
|-- Submissions
|   `-- Users
|       `-- WUSTLKEY
|           `-- WUSTLKEY_COMPLETED_example_assignment.py
`-- Users
    `-- WUSTLKEY
        |-- COPY_ME_example_assignment.py
        `-- COMPLETED_example_assignment.py
```

---

## Recommended Workflow

1. Copy required files from `Assignment_Data/` into `Users/WUSTLKEY/`
2. Make edits and run all code in `Users/WUSTLKEY/`
3. When finished, copy completed files into `Submissions/Users/WUSTLKEY/`

---

## Navigating to the Assignments Directory

To navigate to the main assignments directory, run the following command in your terminal:

```bash
cd /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments
```

To list the available assignments:

```bash
ls -lsh
```

You should see directories named `A01`–`A14`, each corresponding to a weekly assignment.

---

## Notes

- Your WUSTL key directory is created for you — do not rename it
- Do not modify directory permissions
- Do not work directly in `Assignment_Data/`
- If you encounter permission issues, contact the course staff

---


