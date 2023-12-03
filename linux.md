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

### General Commands
man x - manual for X command
whatis x - one line description of X command
apropos - find a command based on a keyword
absolute path - the path of a file from the root directory - cd /home/user/X
relative path - the path in relation to the current working directory - cd X from /home/user
alias newcommand=existingcommand - set an existing command to a new custom command

### Working with directories
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


### Working with files
There are 3 types of files:
1. Regular - images, scripts, configuration / data files
2. Directory - folders
3. Special Files:
   3.1. Character Files - devices under the /dev directory, such as the mouse and keyboard
   3.2. Block Files - hard disks and RAM
   3.3. Links - Hard Links and Soft Links
   3.4. Socket Files
   3.5. Named Pipes
   
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


## System Commands
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

## Network Commands
- ifconfig - returns network data. If not installed - sudo apt install net-tools
- ip a - newer, more detailed version of ifconfig

## Package Manager
- sudo - "super user do" - gives current user priviliges to edit restricted files and operations
- apt - "advanced package manager" install and update software packages
- sudo apt update - check if you have updates to your packages
- sudo apt upgrade - upgrade the available updates if any
- sudo apt install X - install package
- sudo apt remove X - uninstall package

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

### Package Manager
A package manager provides installation, upgrading, and removing packages from the Linux OS. 
- Package managers on Debian distributions:
   - DPKG
   - APT
- Package managers on Red Hat, Fedora, Centos distributions:
   - RPM
   - YUM
   - DNF

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
