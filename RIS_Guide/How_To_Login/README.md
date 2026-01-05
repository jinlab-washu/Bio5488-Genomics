>Created by Elle Mehinovic.
>Last modified [01-05-2025](01-05-2025).

# Ris Guide: How To Login @ BIO5488

* ### Step 1:
  * Identify your WUSTL Key Username and Password:
    * To log into the RIS you must have a WUSTL Key and password\. Your login information will usually match that of your WUSTL Key Login unless specified otherwise\.

<p align="center"><img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login0.png"></p> 

---
* ### Step 2:
  * We must make sure that we can connect to the RIS server before we can login\. This can be achieved three ways:
    * Wi\-Fi:
      * You can automatically connect to the RIS server if you are on WUSTL Secure Wi\-Fi:
        * The “Username” and “Password” to this network will Be your WUSTL Key Login\.   <span style="color:#007360"> _[\(See Previous Step)](slide2.xml)_ </span>  <span style="color:#007360"> </span>
        
        <p align="center"><img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login1.png"></p> 
    
    * VPN  with Cisco Ready Connect \(required\):
      * Follow the following guides\, based on your OS\, to download and install Cisco AnyConnect Client and log into WUSTL’s VPN:
        * Mac Users:
          * [https://bpb\-us\-w2\.wpmucdn\.com/sites\.wustl\.edu/dist/5/1185/files/2018/04/vpn\-Mac\-MED\-new\.pdf](https://bpb-us-w2.wpmucdn.com/sites.wustl.edu/dist/5/1185/files/2018/04/vpn-Mac-MED-new.pdf)
        * Linux Users:
          * [https://bpb\-us\-w2\.wpmucdn\.com/sites\.wustl\.edu/dist/5/1185/files/2018/04/vpn\-Linux\-MED\-new\.pdf](https://bpb-us-w2.wpmucdn.com/sites.wustl.edu/dist/5/1185/files/2018/04/vpn-Linux-MED-new.pdf)
        * Windows Users:
          * [https://bpb\-us\-w2\.wpmucdn\.com/sites\.wustl\.edu/dist/5/1185/files/2018/04/vpn\-Windows\-MED\-new\.pdf](https://bpb-us-w2.wpmucdn.com/sites.wustl.edu/dist/5/1185/files/2018/04/vpn-Windows-MED-new.pdf)
    * Ethernet  Connection \(a Local Area Network \(LAN\) with a network connector\):
      * You will be able to automatically connect to the RIS server if you have  <span style="color:#C00000"> _BOTH_ </span>  <span style="color:#FF0000"> </span> of the following:
        * Your computer/machine is physically on the WUSTL medical school campus
          
          <p align="center"><span style="color:#C00000">       ***   AND   *** </span></p>
        * You are hard wired to the Ethernet port\(s\) located on the walls of a room\.
          * These ports are typically located by outlets and may look something like the following image:
         
            <p align="center"><img width="400"  src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login2.jpg"></p>

---
## SSH INTO WORKSPACE
* ### Step 3 - MacOS:
  * Find your terminal:
  * Mac Users:
    * Locate the <img width="25" src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login3.png"> icon at the top of your desktop:

      <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login4.png">
    * Search for “terminal” and open:
      
      <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login5.png">
* <span style="color:#007360"> _[Skip to Step 4](error:ppt-link-parsing-issue)_ </span>


* ### Step 3 -Linux:
  * Find your terminal:
  * Linux Users:
    * Locate the <img width="30" src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login9.png"> “show application” icon on your desktop:
 
      <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login8.png">
    * Search for “terminal” and open:

    <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login10.png">
* <span style="color:#007360"> _[Skip to Step 4](error:ppt-link-parsing-issue)_ </span>

* ### Step 3 -Windows:
  * Find your terminal:
  * Windows Users:
    * Locate the <img width="30" src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login11.png">  “start” icon on your desktop:
 
      <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login12.png"> 
    * Search for “terminal” and open:

      <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login13.png"> 
* <span style="color:#007360"> _[Skip to Step 4](error:ppt-link-parsing-issue)_ </span>
---
* ### Step 4:
  Open your computer's terminal app\, enter the provided command line\, replacing the placeholders with your information\, and then press  _Enter_ :
  * _Format:_
    *  <span style="color:#7030A0">ssh</span>  <span style="color:#7030A0"><sup>1</sup></span>  <span style="color:#002060"> </span>  <span style="color:#C00000"> _\{WUSTL\_KEY\}_ </span>  <span style="color:#C00000"><sup>2</sup></span>  <span style="color:#002060">@compute1\-client\-</span>  <span style="color:#C00000"> _\[1~4\]_ </span>  <span style="color:#C00000"><sup>4</sup></span>  <span style="color:#002060">\.ris\.wustl\.edu​</span>  <span style="color:#002060"><sup>3</sup></span>
  * _Details:_

      1: <span style="color:#7030A0">ssh</span>  <span style="color:#7030A0">:</span>
      * <span style="color:#002060">The SSH \(Secure Shell\) command is used to establish secure\, encrypted network connections to remote devices or servers for the purpose of secure data communication\, remote command execution\, and other network\-related tasks\.</span>
      * <span style="color:#002060">It is required to login to the RIS</span>
        
      2: <span style="color:#C00000"> _\{WUSTL\_KEY\}_ </span>  <span style="color:#C00000"> :</span>
      * <span style="color:#C00000">Your WUSTL Key Login Username</span>
          
      3: <span style="color:#002060">@compute1\-client\-</span>  <span style="color:#C00000"> _\[1~4\]_ </span>  <span style="color:#002060">\.</span>  <span style="color:#002060">ris\.wustl\.edu</span>  <span style="color:#002060">​</span>  <span style="color:#002060"> </span>  <span style="color:#002060">:</span>
      * <span style="color:#002060">RIS domain name</span>
      
        4: <span style="color:#C00000"> _\[1~4\]_ </span>  <span style="color:#C00000">  </span>  <span style="color:#C00000"> :</span>
        * <span style="color:#C00000">The RIS  has four clients you can log into\. A client is any computer hardware or software device that requests access to a service provided by a server\.</span>
        * <span style="color:#C00000"> _Most users will use client\-1_ </span>
        * <span style="color:#C00000">There is no notable difference between clients\, and they will run identically\.</span>
        
* <span style="color:#007360">	</span>  _Example:_  <span style="color:#007360">​</span>

    <span style="color:#7030A0">ssh</span>  <span style="color:#007360"> </span>  <span style="color:#C00000">Username</span>  <span style="color:#002060">@compute1\-client\-</span>  <span style="color:#C00000">1</span>  <span style="color:#002060">\.ris\.wustl\.edu</span>

> <span style="color:#545454"> _Note:_ </span>
> <span style="color:#545454">Depending on your OS\, your command line will either start with a “%” for Mac users\,  “$” for Linux users\, and “>” for Windows users</span>
---
* ### Step 5:
  You should be prompted to enter your password\. Your password should be your WUSTL Key Login password\, unless started otherwise by RIS:
  * MacOS Terminal:
  
  <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login14.png">


  * Linux Terminal:

  <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login15.png">


  * Windows Terminal:

  <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login16.png">

---
## MOUNT INTO WORKSPACE
* ### Step 3 - Find your Network File Client:

 * #### MacOS:
 
   * Mac Users:
     * Locate the <img width="25" src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login3.png"> icon at the top of your desktop:
 
       <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/How_To_Login/images/RIS_Guide-How_To_Login4.png">
     * Select "GO" -> "Connect to Server..." :
       
       <img height="500" src="https://github.com/LVMEHINOVIC/LabCode/blob/main/BIO5488/COURSE/RIS_Guide/How_To_Login/images/RIS-GUIDE-How-To-Login17.png">
 
     * Paste : smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/COURSE_NAME/Assignments/{ASSIGNMENT_WEEK} into bar (EX: smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00).
        > If prompted enter your WUSTL_KEY and password
       
   
     * Press "Connect" button on bottom right corner
        > If prompted enter your WUSTL_KEY and password
        
       <img  src="https://github.com/LVMEHINOVIC/LabCode/blob/main/BIO5488/COURSE/RIS_Guide/How_To_Login/images/RIS-GUIDE-How-To-Login18.png">
 

 * #### CyberDuck:
 
   * CyberDuck Users:
     * Open CyberDuck and select "SMB (Server Message Block)" from drop down menu
       
     * In server space bar paste : smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/COURSE_NAME/Assignments/{ASSIGNMENT_WEEK} (EX: smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00) this will auto configure.
       
     * In WORKGROUP\Username paste: ACCOUNTS.AD.WUSTL.EDU\{WUSTUL_KEY} (replace with your WUSTL KEY)
 
     * Paste : smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/COURSE_NAME/Assignments/{ASSIGNMENT_WEEK} into bar (EX: smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00).

     * Press "Connect" button on bottom right corner
        > If prompted enter your WUSTL_KEY and/or password
               
       <img  src="https://github.com/LVMEHINOVIC/LabCode/blob/main/BIO5488/COURSE/RIS_Guide/How_To_Login/images/RIS-GUIDE-How-To-Login19.png">
 
 * #### CyberDuck:
 
   * Linux/Windows Users:
     * Open "File Manager" and navigate to your computers "Network" share. 
       
     * In "Connect To Server" Space paste : smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/COURSE_NAME/Assignments/{ASSIGNMENT_WEEK} (EX: smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00) this will auto configure.

        <img  src="https://github.com/LVMEHINOVIC/LabCode/blob/main/BIO5488/COURSE/RIS_Guide/How_To_Login/images/RIS-GUIDE-How-To-Login20.png">

     * Press "Connect" button on bottom right corner, you should have a window pop up asking for more information:
       
     * If you see: WORKGROUP\Username paste: ACCOUNTS.AD.WUSTL.EDU\{WUSTUL_KEY} (replace with your WUSTL KEY) else if you see DOMAIN paste: ACCOUNTS.AD.WUSTL.EDU
       
        <img  src="https://github.com/LVMEHINOVIC/LabCode/blob/main/BIO5488/COURSE/RIS_Guide/How_To_Login/images/RIS-GUIDE-How-To-Login21.png">


     * Press "Connect" button on top right corner
        > If prompted enter your WUSTL_KEY and/or password
        
       
       <img  src="https://github.com/LVMEHINOVIC/LabCode/blob/main/BIO5488/COURSE/RIS_Guide/How_To_Login/images/RIS-GUIDE-How-To-Login19.png">
 ---

## Congratulations you now have logged onto to the Course RIS Space\.
  * [RIS Compute Quick Start Documentation ](https://docs.ris.wustl.edu/doc/compute/compute-quick-start.html)
  * [Jira Accesses ](https://jira.ris.wustl.edu/servicedesk/customer/portal/1/group/22)
    * Ask questions or help with compute
  * [RIS Homepage ](https://ris.wustl.edu/)
  * [Compute Resources](https://ris.wustl.edu/services/compute/resources/)

