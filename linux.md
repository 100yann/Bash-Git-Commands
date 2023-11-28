# Linux

man x - manual for X command

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
- fdisk - manipulate disk partition table
- lsblk - lists block devices
- top - display linux processes
- htop - a better visualization of top. If not installed - sudo apt install htop


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