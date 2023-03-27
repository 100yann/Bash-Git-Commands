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

Repositories (repos) store the full history and source control of a project. They can be stored either locally or hosted online. Most repositories are stored on GitHub, while core contributors make a local copy to work on using push/pull.


Git Commands

git init - makes the current folder a repository
git add filename - add a specified file to the staging area (not committed yet)
git add .  - add all files to staging area
git status - gives you the status of your current git process
git rm -f filename - removes a file from the current staging area (but this also DELETES it)
git rm — cached filename - removes a file from staging area without deleting it
git commit - commit the current changes in the staging area (index) to the master branch
git commit -m - adds message to your commit
git log - returns all previous commits with a log id
git log —oneline - returns all previous commits with a log id but each log id takes up only one line
git checkout log id - goes back to the commit with the specified log id
git revert log id - reverts a commit with the specified log id but adds the revert function in the index ( so you can revert/remove the first revert)
git reset - goes all the way back to a specified lo id and removes other logs
