> Created by Elle Mehinovic.
> Last modified [01-05-2024](01-05-2024).

# Ris Guide: Submitting Jobs

Running Jobs on The RIS
smb://storage1.ris.wustl.edu/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00

- There are three ways to run a job:
  - Directly on the RIS compute cluster
    - Can run smaller/simple commands \(i\.e\. ‘cp’\) and is limited to resources available on the RIS\.
  - Submitting an interactive job
    - Is limited to a 24\-hour running window\, but users can call required resources\.
  - Scheduling a non\-interactive job
    - Is limited to 27 day’s running\, users can call required resources\, job is submitted to queue until resources are available for dispatch\.

---

- ### Step 1:

  - Upon login\, you will always be in your home directory:

    - You can check your current path\, use the _pwd_ command:

        <img src="https://github.com/jinlab-washu/Getting_Started/blob/main/RIS_Guide/Submitting_Jobs%20/images/RIS_Guide-Submitting_Jobs0.png">
      Navigate your own directory following command\, and replacing placeholders with your course name, weekly assignment, and wustl key information:
        * _Format:_
          * cd<sup>1</sup>  /storage1/fs1/workshops/Active/BIO5488/{COURSE_NAME}<sup>2</sup>/Assignments/{ASSIGNMENT_WEEK}<sup>3</sup>/Users/{WUSTL_KEY}<sup>4</sup>
        *  _Details:_

            1: cd:
            * Linux command that will change directories\, ie  _cd_

            2: /storage1/fs1/workshops/Active/BIO5488/{COURSE_NAME}
            * PATH to course directory (EX: /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01)

            3: /Assignments/{ASSIGNMENT_WEEK}:
            * Weekly assignment directory (EX: /Assignments/A00)

            4:  /Users/{WUSTL_KEY}:
            * Your WUSTL Key Login Username

    -     _Example:_
      - cd /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00/Users/WUSTL_KEY

---

## Before Running **_ANY_** Job on the RIS:

- Before you run any interactive or non\-interactive job\, you must export your environment to be visible in the docker environment. **_You must do this step every time!_**
  > ### Step 2:
  >
  > - Run the following to add required paths into docker image\. Similarly\, to the local run flag “\-v”\, each path must be followed by a “:” and a mounted path inside the container\.
  > - If you do not run the following command\, then only the directory which you currently reside in will be mounted inside the docker image\.
  > - You can export as many paths as you want by separating each path by a space:
  >
  > - _Format:_
  >
  >   - export<sup>1</sup> LSF*DOCKER_VOLUMES<sup>2</sup>= "*{/A/PATH}<sup>3</sup>_:_{/A/PATH}<sup>4</sup>\_ _{/ANOTHER/PATH}<sup>5</sup>_:_{/ANOTHER/PATH}<sup>5</sup>_"
  >
  > - _Details:_
  >
  >   1: export:
  >
  >   - The \`export\` command in a Unix\-like shell is used to create or modify environment variables\, making them available for use by subsequent commands and processes in the current shell session\.\.
  >
  >   2: LSF_DOCKER_VOLUMES= "_\{/A/PATH\}_ : _\{/A/PATH\}_ _{/ANOTHER/PATH}:{/ANOTHER/PATH}_":
  >
  >   - \`LSF_DOCKER_VOLUMES\` creates a link between files on the RIS and in the folder in the docker container\. Your Folder location needs to be followed by a “:” and the location you would like to folder to be accessible inside the docker container \(does not need to be identical to the RIS folder location but it’s recommended to keep identical\)\. Each new location must be separated by a space\.
  >
  >     3,4&5\. _\{/path/to/directory\}_: _\{/path/to/directory\}_
  >
  >     - Allows for your RIS directory \(ie \#3\) to be accessed inside the docker container given the path \(ie \#4\)\.
  >     - More paths can be added with a new space and repeating the following pattern \(ie \#5\)\:
  >       - RIS location, “:” , Docker Location
  >
  > - _Example:_
  >
  >   - export LSF_DOCKER_VOLUMES="$HOME:$HOME /storage1/fs1/workshops/Active/BIO5488:/storage1/fs1/workshops/Active/BIO5488"

> ** Note: $HOME is a variable unique to all RIS users\, and it is a special directory that houses all your user files \(ie ~\.bashrc\, \.env\, etc\.\)\. You do not have to add this into your export command\. **

---

## Running Interactive Jobs:

> ### Step 3:
>
> Interactive jobs act like your current terminal\, but within a docker’s environment\.
>
> - _Format:_
>   - bsub<sup>1</sup> –q<sup>2</sup> general-interactive<sup>3</sup> –Is<sup>4</sup> –G<sup>5</sup> {GROUPNAME}<sup>6</sup> –a<sup>7</sup> 'docker(_{DOCKER_IMAGE}<sup>9</sup>_ /_{REPO}<sup>10</sup>_ :_{VERSION}<sup>11</sup>_ ) '<sup>8</sup> /bin/bash<sup>12</sup>
> - _Details:_
>
>   1: bsub
>
>   - Submits a job to LSF by running the specified command and its arguments\.
>
>     2: \-q :
>
>     - Flag to set which queue the job should run in.
>
>       3: general\-interactive
>
>       - The queue name; in this case an interactive queue named “general\-interactive”
>
>     4: \-Is :
>
>     - Submits an interactive shell
>
>     5: \-G :
>
>     - Indicates what compute group the user and job belongs to.
>
>       6: _\{GROUPNAME\}_
>
>       - The compute group the user belong to
>
>     7: \-a :
>
>     - Flag call docker\.
>
>       8: 'docker \(_\{DOCKER_IMAGE\}_ / _\{REPO\}:_ _\{VERSION\}_ \) '
>
>       - Format for calling a docker image
>
>         9,10,&11 _\. \{DOCKER_IMAGE\}_ / _\{REPO\}_: _\{VERSION\}_
>
>         - A docker image name\, followed by _“/”_ and the docker repository\, “ _:_ ” \, and tag
>         - This all can be found on the image’s docker hub page\.
>
>     12: /bin/bash : \* Opens a bash shell to run executables docker\.
>
> - _Example:_
>
>       bsub –q general-interactive –Is –G compute-workshop –a 'docker(jinlab/basic:vs1)'  /bin/bash

---

## Running Non\-Interactive Jobs:

> ### Step 4:
>
> Interactive jobs act like your current terminal\, but within a docker’s environment\.
>
> - _Format:_
>   - bsub<sup>1</sup> –q<sup>2</sup> general<sup>3</sup> –R 'rusage\[mem=\#\] ' <sup>4</sup> –G<sup>5</sup> _\{GROUPNAME\}_ <sup>6</sup> –a<sup>7</sup> 'docker _\(\{_ _DOCKER_IMAGE\}_ <sup>9</sup> _/_ _\{REPO\}_ <sup>10</sup> : _\{VERSION\}_ <sup>11</sup>
> - _Details:_
>
>   1: bsub
>
>   - Submits a job to LSF by running the specified command and its arguments\.
>
>     2: \-q :
>
>     - Flag to set which queue the job should run in\.
>
>     3: general\-interactive
>
>     - The queue name; in this case an interactive queue named “general\-interactive”
>
>     4: \-R :
>
>     - Requests resources for jobs execution
>       - 'rusage\[mem=\#\] '
>         - Requests how much memory is needed for the job to execute\.
>
>     5: \-G :
>
>     - Indicates what compute group the user and job belongs to\.
>
>       6: _\{GROUPNAME\}_
>
>       - The compute group the user belong to
>
>     7: \-a :
>
>     - Flag call docker\.
>
>     8: 'docker _\(_\{_DOCKER_IMAGE\}_ / _\{REPO\}_: _\{VERSION\}_ \) '
>
>     - Format for calling a docker image
>
>       9,10,&11\. _\{DOCKER_IMAGE\}_ / _\{REPO\}_: _\{VERSION\}_
>
>       - A docker image name\, followed by “/” and the docker repository\, “ : ” \, and tag
>       - This all can be found on the image’s docker hub page\.
>
>     12: _\{ARG\}_ :
>
>     - Execution argument\.
>       - Could be /bin/bash\, followed by a bash script1\, shell script2\, or executable3\.
>         - /bin/bash bsub_run\.sh
>         - /bin/bash –c '\(~~~\) '
>         - /bin/bash mkdir -p /storage1/fs1/workshops/Active/BIO5488/SP2026.L41.BIOL.5488.01/Assignments/A00/Users/WUSTL_KEY
>         - Can also be just an executable
>
> - _Example:_
>
>       bsub –q general –Is –G compute-workshop –a 'docker(jinlab/basic:vs1)'  /bin/bash  -c ' (echo  "Hello World"  >> example_docker_job.txt)'

---

RIS utilizes IBM Spectrum LSF\, a workload manager and job scheduling software in HPC’s\, users can run most LSF commands\. Below are a few simple LSF commands\, their functions\, and examples you can test:

- bqueues
  - Displays information about queue
    - bqueues
- bgadd
  - Creates a job group for a specific user; the ‘\-L’ flag specifies how many jobs can run at a time in your job group
    - bgadd –L 50/ _\{WUSTL_KEY\}_ /a_unique_job_group_name
- bgmod
  - Modify the number of jobs that can run inside the specified job group; the ‘\-L’ flag specifies how many jobs can run at a time in your job group
    - bgmod –L 10 / _\{WUSTL_KEY\}_ /a_unique_job_group_name
- bjgroup
  - Displays information about job groups; the ‘\-s’ flag can be used to see specific job group
    - bjgroup –s / _\{WUSTL_KEY\}_ /a_unique_job_group_name
- bsub
  - Submits a job to LSF by running the specified command and its arguments\.
- bjobs
  - Displays and filters information about LSF jobs\. Specify one or more job IDs \(and\, optionally\, an array index list\) to display information about specific jobs \(and job arrays\)\.
    - bjobs
- btop
  - Move a pending job relative to the first job in the queue\.
    -     btop  _\{JOBID\}_
- bkill
  - Sends signals to kill\, suspend\, or resume unfinished jobs; the ‘\-u’ flag can be used to specify a user and ‘0’ will kill all jobs by that user; the ‘\-g’ flag can be used to specify a user’s job group and ’0’ will kill all jobs in that group only
    - bkill _\{JOBID\}_
    - bkill -u _\{WUSTL_KEY\}_ 0
    - bkill –g _\{WUSTL_KEY\}/a_unique_job_group_name_ 0
