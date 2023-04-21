Learning Git and Bash Terminal

Git is a version control software that lets you keep track of versions of your code.
GitHub is an online repository that lets you store your gits.


Bash Commands  
cd x - change directory to x (needs to be directly accessible from current directory)  
cd ~ - go back to home directory  
cd .. - goes back one level  
clear - clears screen of previous commands  
ls - list contents of directory  
mkdir - make a folder within your current dir  
rm x- remove file x  
rm -rf x - remove folder x  
touch x.extension - makes a file  
pwd - print working directory (the directory you're currently in)  

Repositories (repos) store the full history and source control of a project. They can be stored either locally or hosted online. Most repositories are stored on GitHub, while core contributors make a local copy to work on using push/pull.  


Git Command  

git init - makes the current folder a repository  
git add filename - add a specified file to the staging area (not committed yet)  
git add .  - add all files to staging area  
git status - gives you the status of your current git process  
git rm -f filename - removes a file from the current staging area (but this also DELETES it)  
git rm — cached filename - removes a file from staging area without deleting it  
git commit - commit the current changes in the staging area (index) to the master branch  
git commit -m - adds message to your commit  
git commit -a -m - commits all unsaved changes and adds message  
git log - returns all previous commits with a log id  
git log —oneline - returns all previous commits with a log id but each log id takes up only one line  
git checkout log id - goes back to the commit with the specified log id  
git checkout HEAD~int - goes back int times before the last commit  
git checkout HEAD <filename> - goes back to the last commit and deletes all uncommitted changes  
git switch -    - reverts the checkout command and goes back to the previous head  
git revert log id - reverts a commit with the specified log id but adds the revert function in the index ( so you can revert/remove the first revert)  
git reset - goes all the way back to a specified lo id and removes other logs  
git commit --amend - update/edit the message or files of your previous commit  
git push -u main - pushes your local repository to github  
git branch - view all existing branches  
git branch X - creates a new branch with the name X  
git branch -v - displays all existing branches with more info about them  
git switch X - switches to an existing branch  
git switch -c X - creates and switches to branch X  
git branch -d X - delets branch X, only possible if you're not currently on specified branch  
git branch -m X - rename the branch you're currently on to X  
git merge X - merge branch X with your current branch  
git diff - returns all changes made in the current working directory that aren't staged  
git diff HEAD - same but both staged and unstaged changes  
git diff --staged/--cached - shows all staged changes  
git diff HEAD [filename] - returns changes in specific file  
git diff branch1..branch2 - returns changes between the 2 branches  
git diff commit1..commit2 - same but for commits  
git stash - save uncommited changes so you can change branches without conflicts/commiting your changes/losing them. You can stash multiple times  
git stash list - used if you have multiple stashes at the same time  
git stash apply stash@{X} - apply the stash with the specified index  
git stash pop - remove the most recently stashed changes and apply them to your working copy  
git stash apply - apply whatever is stashed but it doesn't remove it from the stash itself  
git stash drop / git stash drop stash@{X}- delete the last stash / specified stash  
git stash clear - clear all stashes  

  
adding a file/directory within a .gitignore file will stop git from tracking changes to these files and commiting them; asterisk *.extension* will ignore all files with the specified extension, folder/ will ignore an entire directory

  
GIT STYLE  
  
Instead of commiting multiple changes in one single commit, organize your commits by functions so that the program/changes are easier to track and if necessary modify.    Git docs recommends describing changes in present tense, imperative style
