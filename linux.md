# Linux

### Kernel 
The main layer between the OS and hardware of the computer. 
The kernel is responsible for 4 key tasks:
1. Memory Management
2. Process Management
3. Device Drivers
4. Systel Calls and Security

##### Memory Management
Memory is divided in two:
1. Kernel Space - the portion of memory that the Kernel uses to execute its services
2. User Space - all processes (user programs) outside of the Kernel Space.

User programs get access to data or allocated in memory by making **system calls** to the kernel which communicates with the hardware to handle the request.
   
- uname -r - return the kernel version

---

### General Commands
- man x - manual for X command
- whatis x - one line description of X command
- apropos - find a command based on a keyword
- alias newcommand=existingcommand - set an existing command to a new custom command

---

### Working with directories
absolute path - the path of a file from the root directory - cd /home/user/X

relative path - the path in relation to the current working directory - cd X from /home/user


- pwd - print working (current) directory
- cd - change directory. If it has no arguments it takes you to your home directory. 
- ls - list directory contents
- ls -a - show hidden files as well
- ls - l - shows more info about the files/folders in a list format
- ls -lh - shows more info in human readable format (file size)
- mkdir - make a new folder
- mkdir -p ParentFolder/ChildFolder - create multiple folder deep
- rmdir x - remove x folder if it's empty
- rmdir -p - remove directory tree
- rm -rf - this command will also delete a folder. -r stands for recursively and -f for force 

---

### Working with files
There are 3 types of files:
1. Regular - images, scripts, configuration / data files
2. Directory - folders
3. Special Files:
      - Character Files - devices under the /dev directory, such as the mouse and keyboard
      - Block Files - hard disks and RAM
      - Links - Hard Links and Soft Links
      - Socket Files
      - Named Pipes
   
- rm - remove file
- file X - returns X's file type
- touch - create a file
- cp X X2- copy fileX as fileX2
- cp X path - copy fileX to a new folder
- cp -r dir path - copy a folder to a new path
- mv x path - move/rename file
- head x - returns the first 10 lines of a file
- tail x - returns the last 10 lines of a file
- cat x - returns all the contents of a file
- echo text >file - add text into a file
- cat > filename - allows you to input text when creating a file, to save use ctrl+d
- more filename - breaks down large files into pages for easier viewing
- less filename - opposite of more
- du -sk filename / ls-lh filename - display the size of a file


---

### System Commands
- uptime - how long the system has been running
- free - returns amount of free and used memory in the system
- ps -A - a snapshot of current processes 
- df - return used and available disk space
- df -hP
- fdisk - manipulate disk partition table
- lsblk - lists block devices
- top - display linux processes
- htop - a better visualization of top. If not installed - sudo apt install htop
- history - show command history
- env - show list of environment variables
- export VARIABLE=value - make a new env variable for the current shell instance
- echo 'export PROJECT=MERCURY' >> ~/.profile - save the env variable in .profile to make it persistent
- dmesg - print or control the kernel ring buffer
- udevadm info --query=path --name=/dev/device - gives details about a device
- lspci - display information about all PCI devices
- lsblk - display information about disk devices
- lscpu - display detailed info about the cpu
- lsmem --summary - display available memory in the system
- free -m - display the free vs used memory in MB
- lshw - display info about the hardware of the computer

---

### Network Commands
- ifconfig - returns network data. If not installed - sudo apt install net-tools
- ip a - newer, more detailed version of ifconfig

---

### Linux Directories 
- /dev - installed devices show up in this directory
- /opt - stores any third party programs
- /mnt - used to mount file systems temporarily
- /tmp - used to store temporary data
- /media - all external media is mounted under /media.
- /bin - basics programs and binary
- /etc - most of the configuration files in linux
- /lib - shared libraries
- /usr - all user applications and user data
- /var - directory where the system stores log

---

### Linux Boot Sequence
1. BIOS POST
2. Boot Loader
3. Kernel Initialization
4. INIT Process

Systemd target - what interface your Linux OS displays. runlevel 5 boots a GUI, runlevel 3 boots a terminal
- runlevel - check what runlevel your systemd is using
- systemctl get-default - return the default target of the systemd
- systemctl set-default multi-user.target/graphical.targert - set the default target to a terminal/GUI interface respectivelly
- ls -l /sbin/init - check the init process of the systemd

---

### Package Manager
A package manager provides installation, upgrading, and removing packages from the Linux OS. 
- Package managers on Debian distributions:
   - DPKG
   - APT
- Package managers on Red Hat, Fedora, Centos distributions:
   - RPM
   - YUM
   - DNF
     
- sudo - "super user do" - gives current user priviliges to edit restricted files and operations

##### RPM Commands
- rpm -ivh package name - install a package
- rpm -e package name - remove a package
- rpm -Uvh package name - upgrade package
- rpm -q package name - get details about an installed package
- rpm -Vf path to file - verifies the package is installed successfully
  
##### YUM Commands
YUM works on RPM distributions
- yum install package
- yum repolist - display all repos installed on the system
- yum provides argument - check which package should be installed based on the command passed as an argument
- yum remove package
- yum update package
- yum update - checks all packages and marks any that can be updated

##### DPKG (Debian Package Manager)
- dpkg -i package name - install
- dpkg -r pn - uninstall
- dpkg -l pn - list
- dpkg -s pn - status
- dpkg -p path to file - verify/ check version number

##### APT
Relies on DPKG. Automatically resolve dependency issues when installing packages
- apt install name
- apt remove name
- apt search name
- apt list
- apt update - update all packages
- apt upgrade - install available updates if any
- apt edit-sources - opens the /etc/apt/sources.list in a text editor
You can add more repositories by updating the sources.list file

---

### Working with Shell
##### Archiving Files
- tar -cf name.tar file1 file2 file3 - tar -c creates an archive -f allows us to specify the name of the archive
- tar -tf name.tar - display the contents of the archive
- tar -xf name.tar - extract the contents
- tar -zcf name.tar files - compress the size of the archive

##### Compressing Files
There are 3 popular commands used for compression - the compression command will add a compression extension to the file - it can be uncompressed afterwards:
- bzip2 filename - .bz2 - bunzip2
- gzip filename - .gz - gunzip
- xz filename - .xz - unxz

You can read compressed files without uncompressing them using **zcat / bzcat / xzcat** filename

##### Searching for Files and Directories
- locate file/dir - locates and returns the path to the file/dir specified
- updatedb - updates the database so locate finds recently-created files/folders
- find dir -name filename - search for a file by name
- grep searchpattern filename - search within a file for a match with the searchpattern
- grep -i - case insensitive search
- grep -r searchpattern directory - search for a pattern in the directory recursivelly, doesn't need a file as an option, and will return all files that match
- grep -v searchpattern filename - returns a file that **does not** match the searchpattern
- grep -w searchpattern filename - searches for a whole word, instead of characters
- grep -A1 searchpattern filename - return the line matching the pattern, and the line under the matching line
- grep -B1 searchpattern filename - same but previous line
- grep -A1 -B1 searchpattern filename - same but both lines

##### IO Redirection
There are 3 data streams in Linux:
1. Standard Input - stdin - data is sent to and read by the program
2. Standard Output - stdout - data sent by the program
3. Standard Error - stderr - errors sent by the program

- echo $SHELL > filename.txt - redirect stdout to a file instead of the terminal. This will overwrite the contents of the file
- echo $SHELL >> filename.txt - same but appends to the file
- cat missing_file 2> error.txt - redirect stderr to a file
- cat missing_file 2>> error.txt - same but append
- cat missing_file 2> /dev/null - your program will not display/store errors

##### Command Line Pipes
Link together commands:  
```
sample.txt = Hello there!\nNice to see you!  
grep Hello sample.txt | less
```
less will return only "Hello there", since that was the only input received from grep Hello sample.txt  
- echo $SHELL | tee filename.txt - redirect stdout to a file and display it in the terminal. This will overwrite the contents of the file.
- echo $SHELL | tee -a filename.txt - same but append input to contents

##### VI Editor
The VI editor has 3 modes:
1. Command Mode - a file is opened in command mode by default. To switch to insert mode, type lowercase `i`. To switch to last line, click `:` key
- press `yy` to copy a line
- press `p` to paste a line
- `ZZ` to save a file
- `x` to delete a letter
- `dd` delete a whole line
- `dINTd` delete int amount of lines
- `u` undo
- `ctrl r` redo
- `/pattern` find a word that matches pattern from all text after the cursor while `?line` does this for all text before the cursor
- `n` move down to next occurence of a match for `/`, move up to next match for `?`
- `N` move up to next occurence for `/`, move down for `?`
2. Insert Mode - allows you to add text. To switch back to command mode, click the `escape` key
3. Last Line - allows you to save file, discard changes, exit. To switch back to CM, click the `escape` key
- `:w` - write to file
- `:q` - quit file
- `:wq` - write and quit file
- `:q!` - quit without confirmation
   
- vi /home/user/filename.txt - open or edit a file inside VI editor
**VIM is an improved version of VI**
