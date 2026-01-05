>Created by Elle Mehinovic.
>Last modified [01-05-2024](01-05-2024).
# Ris Guide: Navigating Directories Tour

This is a guided tour of all major directories available to users while logged onto the RIS\. Each directory’s purpose and layout will be explained\, so please follow along via your command line\.

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
  
  <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating0.png">
  
  * Linux Terminal:
 
  <img width="1000" src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating1.png">
  
  * Windows Terminal:
 
  <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating2.png">


---

* ### Step 2:
  * Once you have logged into the RIS your will see YOUR home directory:
      * You can check your current path\, use the  <span style="color:#7030A0"> _pwd_ </span>  <span style="color:#7030A0"> </span> command:
   
        <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating3.png">
        
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

## The Jin Lab Active Space

* Step 3:
  * We are now going to navigate to our main active space:
      * To navigate through different directories\, we will be using the  <span style="color:#7030A0"> _cd _ </span> command followed by the active space path\.
        * In your terminal copy the following command and hit enter:
         
          ``` bash
          cd  /storage1/fs1/jin810/Active
          ```


        * After run the following command to list the current directory contents:
          
          ``` bash
          ls -lsh  /storage1/fs1/jin810/Active
          ```
    * You will find that there are four main directories inside our active space: 	 <span style="color:#0000FF">Projects\, References\, testing\, and U19\_Data\_Core\.</span>
      
        <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating4.png">

---

### Active Space and Directories
  * What is the “Active Space”?
    * Active space refers to any directories and subdirectories located in  <span style="color:#002060">/storage1/fs1/jin810/Active</span> \. This is where users may run jobs and store data\.
  * How should I use the “Active Space”?
    * The “Active Space” itself can be a mount point for LSF jobs but users should not be writing to the top\-level active location\, ie  <span style="color:#002060">/storage1/fs1/jin810/Active\.</span>  Instead\, users should use one of the four top level directories in their respective manner\.
  * What are each of the top\-level directories for?
    * Projects
      * The “Projects” folder is where users put information regarding a project that is collaborative\, raw data\, execution scripts\, or finished\.
    * References
      * The “References”  folder holds data that is repeatedly used by multiple individuals
    * testing
      * The “testing” folder is where users will make their own personal directories\. Users can use their directory however they see is best fit\. Most users use this directory for testing purposes\, but  _ALL RAW DATA\, FINAL DATA\, AND SCRIPTS SHOULD BE INSIDE THE PROJECTS FOLDER_ \.
    * U19\_Data\_Core
      * This directory is for the U19 Data Core and some users may not have access to it


  * How do I set up a folder inside the Projects directory?
    * Here is an example of what the formatting inside a folder may be:
      * _ANALYSIS:_
        * Where analysis’s can be stored\. This includes presentations\, or any final conclusions\.
      * _ARCHIVE:_
        * Where to store data not needed anymore\, preferably compressed\.
      * _CODE:_
        * Code used to run any analysis or results\.
      * _INPUT\_FILES:_
        * Any input file needed including raw data\.
      * _MISC:_
        * Can be used for testing\, or however the users see fit\.
      * _RESULTS:_
        * Raw outputs from any code that was ran\.

<img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Navigating_Directories_Tour/images/RIS_Guide-Navigating5.png">

---
* ### Step 4:
  * Currently we have two separate archive storage spaces:
  * Either space is for saving closed projects\, raw data\, and other miscellaneous things\. The difference between the two spaces is the first active space is new while the second is our previous space\. Do not do anything here unless told otherwise\.

<span style="color:#002060">/storage1/fs1/jin810/Archive</span>  <span style="color:#002060">	</span> & <span style="color:#002060">/storage1/fs1/jin810\_archive\_fs1/Archive</span>

