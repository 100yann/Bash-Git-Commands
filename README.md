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
git checkout HEAD tildesign int - goes back int times before the last commit  
git checkout HEAD filename - goes back to the last commit and deletes all uncommitted changes  
git commit --amend - update/edit the message or files of your previous commit  
git branch - view all existing branches  
git branch X - creates a new branch with the name X  
git branch -v - displays all existing branches with more info about them  
git switch X - switches to an existing branch  
git switch -c X - creates and switches to branch X  
git switch -    - reverts the checkout command and goes back to the previous head   
git branch -d X - delets branch X, only possible if you're not currently on specified branch  
git branch -m X - rename the branch you're currently on to X  
git branch -r - view the remote branches my local repo knows about  
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
git restore filename - restores the file to the last commit, deleting all uncommitted changes  
git restore --source HEAD tildesign X filename - restores the file to X commits before your last commit  
git reset - resets repository to specific commit. Will delete all commits that followed the specific commit but doesn't delete the changes made within those commits  
git reset --hard - does the same but deletes the changes as well  
git revert githash - creates a new commit where the changes from specified githash are deleted but the commit itself isn't  
  
If you want to reverse some commits that other people already have on their machines, you should revert instead of reset. If you want to reverse commits that you made but aren't shared yet - you can use reset.  
  
git remote -v - returns any existing remotes for your repository  
git remote add [name(will be used as reference for the url)] [url] - adds a new remote to the current repository, used when you already have code written that you want to push to a GitHub repo  
git remote rename [oldname] [newname] - renames the specified remote  
git remote remove [name] - deletes the specified remote  
git push [remote] [branch] - pushes(uploads) the specified branch to the remote  
git push -u remote branch - will set the upstream, so your repo will remember which remote to push to afterwards and you can only use "git push"  
git push [remote] [local-branch]:[remote-branch] - pushes specified local branch to a specific branch on GitHub  
git clone url - used when you have a GitHub repo that you want to pull(clone) to your local repo  
If you clone a GitHub repo with multiple branches, if you use "git branch" in your local repo you'll only see the main/master branch but with "git branch -r" you'll see all other branches from the GitHub repo. To connect/switch to those you can simply use "git switch [branch-name]"  
fork a github repo - this will make a duplicate repo in your own github profile so you can freely work with it without having to go through pull requests/protection of the original github repo  

git branch -M main - renames your current branch to main, which is the standard branch name for GitHub, as opposed to master  
git fetch [remote] - downloads the latest changes made to a remote repository, without having to merge those changes to your local repository. If [remote] is not specified, it defaults to origin  
git fetch [remote] [branch] - downloads from a specific branch 
git pull [remote] [branch] - same as fetch but automatically integrates those changes to your working directory. If [remote] or [branch] aren't specified it will default to origin and whatever your current branch is tracking respectivelly  

git rebase - used as an alternative to merging or a cleanup tool. It will move or combine a sequence of commits to a new base commit. If you have a main and secondary or more branches, when you merge you will continue having your linear secondary or more branches, going parallel with your main branch. With rebase, your secondary branch will start from the end of the main branch. Rebasing will recreate all your secondary branch commits on the tip(end) of the main branch. *Never rebase commits that are already shared with others.*

  
adding a file/directory within a .gitignore file will stop git from tracking changes to these files and commiting them; asterisk *.extension* will ignore all files with the specified extension, folder/ will ignore an entire directory

  
GIT STYLE  
  
Instead of commiting multiple changes in one single commit, organize your commits by functions so that the program/changes are easier to track and if necessary modify.    Git docs recommends describing changes in present tense, imperative style
