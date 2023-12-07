# Linux

### Kernel 
The main layer between the OS and hardware of the computer. 
The kernel is responsible for 4 key tasks:
1. Memory Management
2. Process Management
3. Device Drivers
4. Systel Calls and Security

#### Memory Management
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
     
- `sudo` - "super user do" - gives current user priviliges to edit restricted files and operations. The default configuration for the sudo command is in `/etc/sudoers` and can be edited with `visudo`

#### RPM Commands
- rpm -ivh package name - install a package
- rpm -e package name - remove a package
- rpm -Uvh package name - upgrade package
- rpm -q package name - get details about an installed package
- rpm -Vf path to file - verifies the package is installed successfully
  
#### YUM Commands
YUM works on RPM distributions
- yum install package
- yum repolist - display all repos installed on the system
- yum provides argument - check which package should be installed based on the command passed as an argument
- yum remove package
- yum update package
- yum update - checks all packages and marks any that can be updated

#### DPKG (Debian Package Manager)
- dpkg -i package name - install
- dpkg -r pn - uninstall
- dpkg -l pn - list
- dpkg -s pn - status
- dpkg -p path to file - verify/ check version number

#### APT
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
#### Archiving Files
- tar -cf name.tar file1 file2 file3 - tar -c creates an archive -f allows us to specify the name of the archive
- tar -tf name.tar - display the contents of the archive
- tar -xf name.tar - extract the contents
- tar -zcf name.tar files - compress the size of the archive

#### Compressing Files
There are 3 popular commands used for compression - the compression command will add a compression extension to the file - it can be uncompressed afterwards:
- bzip2 filename - .bz2 - bunzip2
- gzip filename - .gz - gunzip
- xz filename - .xz - unxz

You can read compressed files without uncompressing them using **zcat / bzcat / xzcat** filename

#### Searching for Files and Directories
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

#### IO Redirection
There are 3 data streams in Linux:
1. Standard Input - stdin - data is sent to and read by the program
2. Standard Output - stdout - data sent by the program
3. Standard Error - stderr - errors sent by the program

- echo $SHELL > filename.txt - redirect stdout to a file instead of the terminal. This will overwrite the contents of the file
- echo $SHELL >> filename.txt - same but appends to the file
- cat missing_file 2> error.txt - redirect stderr to a file
- cat missing_file 2>> error.txt - same but append
- cat missing_file 2> /dev/null - your program will not display/store errors

#### Command Line Pipes
Link together commands:  
```
sample.txt = Hello there!\nNice to see you!  
grep Hello sample.txt | less
```
less will return only "Hello there", since that was the only input received from grep Hello sample.txt  
- echo $SHELL | tee filename.txt - redirect stdout to a file and display it in the terminal. This will overwrite the contents of the file.
- echo $SHELL | tee -a filename.txt - same but append input to contents

#### VI Editor
**VIM is an improved version of VI**
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

```
vi or vim /home/user/filename.txt
```
Open or edit a file inside VI editor
```
editor
```
Check which editor is default

---

### Network
#### DNS 
**Name Resolution** - checking if a name matches an ip in /etc/hosts
- cat >> /etc/hosts ip - name - save an ip address under a name
- ping name/ip - check the network connectivity between host and server/host
- nslookup - query a host name from a DNS server, does not consider the entries in /etc/hosts
- dig - returns more details
  
To avoid adding too many entries into multiple systems, usually all entries are kept on a DNS server. All hosts point to that server by going into /etc/resolv.conf and adding `nameserver serverip`. A system can still have entries inside its /etc/hosts, and it will first check that before checking the DNS server. To change the order, go into /etc/nsswitch.conf and alter `hosts: dns files`

You can also add another entry into your DNS server - `nameserver 8.8.8.8` which is a nameserver hosted by Google that knows about all websites on the internet. This will allow your system to ping external sites hosted on the internet.

When you have multiple subdomains, you can access them more easily by adding `search domain name` in `/etc/resolv.conf`
For example:
```
/etc/hosts = 192.168.1.1 web.company.com
ping web will return an error
/etc/resolv.conf = search company.com
ping web will work successfully
```

**Record Types**
- Storing IP to host names is known as A records
- Storing IPv6 to host names is AAAA records (quad records)
- Mapping 1 name to another name is CNAME records - multiple names for the same application

#### General Networking Concepts

1. Switching - creates a network between 2 systems to connect them.
   - `ip link` - list and modify interfaces on the host
   - `ip addr` - see the ip address of those interfaces
   - `ip addr add ipofswitch` - connect to the switch
   - `ip link set dev name up` - turn on an interface
     
2. Router - connect networks together. It is assigned as many IPs as the number of network it connects
   - `route` - check the routing configurations of the network
     
3. Gateway - creates a route from the network to the router
   - `ip route add ipofnetwork via ipofrouter` - set up the gateway from the network to the router
   - `ip route add default via ipofrouter` - add this router as the default gateway to other networks

These changes are valid until the system restarts. To save these changes, they need to be added to /etc/network/interfaces file
- `hostname -i` - check your system's ip
- `telnet servername portnum` - check the status of a port

#### Troubleshooting
- `traceroute ip` - trace the devices through which the connection goes through. It will show if there's an issue with a device

---

### Security and File Permissions
The information about a user is stored in `cat /etc/passwd`
- `uid` - a unique id for each linux user
- `id username` - check UID, GID
- `grep -i username /etc/passwd` - check the home dir and default shell associated with a user
- `who` - see a list of currently logged in users
- `last` - displays a record of all logged in users

Groups - a collection of Linux users. Each group has a unique id called `gid`

#### Access Control Files
`grep -i ^user dir`
- `/etc/passwd` - the returned data is formatted as follows: USERNAME:PASSWORD:UID:GID:GECOS:HOMEDIR:SHELL
- `/etc/shadow` - stores user passwords - The returned data is formatted as follows: USERNAME:PASSWORD:LASTCHANGE:MINAGE:MAXAGE:WARN:INACTIVE:EXPDATE
- `/etc/group` - stores info about groups - NAME:PASSWORD:GID:MEMBERS

#### Managing Users
- `useradd username` - add a new user
- `passwd username` - add password for the user
- `whoami` - returns the current user
- `passwd` - change your own password
- `userdel username` - delete a user
- `groupadd -g GID name` - create a new group. `-g` allows you to specify a custom group id.
- `groupdel groupname` - delete a group
  
##### Useradd common options:
- `-c` - custom comments
- `-d` - custom home directory
- `-e`- expiry date
- `-g` - specific GID
- `-G` - create user with multiple secondary groups
- `-s` - specify login shells
- `-u` - specific UID

#### File permssions
- `chown username:group file` - change the owner of a file to username and add group. If a group is not provided, only the ownership is changed.
- `chown -R` - recursivelly change the owner of a folder and files and folders inside it.
- `chgrp groupname file` - change the group of a file
  
```
ls -ld folder
OR 
ls -l bash-script.sh
returns -rwxrwxr-x ...
```
1. The first three characters `rwx` are the permissions for the owner of the file = u.
2. The next three `rwx` are the permissions for the group owning the file = g.
3. The last three characters `r-x` are the permissions for all other users = o.
**`r` = read/4, `w` = write/2, `x` = execute/1, `-` = no permission/0.**

- `chmod <permissions> file` - change the permissions of a file
- `chmod u+rwx file` - full access to the owner
- `chmod ugo+r-x file` - read access to owner, group and other users, remove execute access
- `chmod o-rwx file` - remove all permissions for other users
- `chmod u+rwx,g+r-x,o-rwx` - full access for owner, read access for group and remove execute access, no access for other users

Permissions can also be changed by using the octal values of permissions:
- `chmod 777 file` - full access to all users
- `chmod 555 file` - read and execute access to all users
- `chmod 660 file` - read and write access for owner and group, no access for other users
- `chmod 750 file` - full access for user, read and execute for group, no access for other users

#### SSH 
Used to login and execute commands on a remote system. To work, the remote system should have an SSH service running and port 22 be accessible. There should also be a valid user you can use on the remote system or an SSH key.
- `ssh hostname OR ipaddress`
- `ssh user@hostname OR ipaddress`

Passwordless SSH - the remote system has a private key, you have a public key which you use to access the remote system.
- `ssh-keygen -t rsa` - generate a key pair.
- `/home/user/.ssh/id_rsa.pub` - the public key
- `/home/user/.ssh/id_rsa` - the private key
- `ssh-copy-id user@host or ip` - connect remotely using the key pair, will be prompted for a password the first time only. The public key will be installed on the remote system inside `/home/user/.ssh/authorized_keys`
- `Ctrl + D` - quit ssh session

#### SCP
- `scp localdir hostname:dir` - Allows you to copy files to and from a remote server. `-pr` - allows you to copy directories

