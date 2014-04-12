exosome
=======


Hi! This is the Exosome modeling repository.

using git in a nutshell
-----------------------

Instructions on how to use it:

download the repository:

```
git clone http://github.com/salilab/exosome.git
```

All the following commands works anywhere (any directory) within the repository

to update your repository 

```
git pull
```


After you modified the repository, you want to upload your modifications:
to see if anything is modified:

```
git status
```

to add new files to the repository:

```
git add filename
```

to locally commit files that have been modified and have been already added:


```
git commit filename -m "commission comment"
```

to push your changes to the remote repository

```
git push origin master
```

Sometimes you'll be asked to merge....
therefore after you `git commit filename -m "comment"`, then do `git pull` and then `git push origin master`


Important notes
---------------


If you want to modify the modeling script, just duplicate the modeling directory, eg, let's say you want a new modeling directory modeling-2, then `cp -r modeling-1 modeling-2`, do your modifications in modeling-2, `git add modeling-2` your new directory, `git commit modeling-2 -m "added a new modeling directory"`, and then `git pull`. *Never* modifiy current modeling directories, because they represent runs in the cluster. Just keep adding stuff.

Submission Script
-----------------
(Not yet there)
Within each modeling directory, there is a python script called `makejobs.py` when called with python `python makejobs.py` it will automatically create directories specified in the script, copying the template directory, into new directories that will contain the runs. `makejobs.py` will also specify running parameters to be passed to each `modeling.py` script contained in the newly created directory. `makejobs.py` also create a `job.sh` file with all needed variables. To submit the job `qsub job.sh` within each directory.

Questions, comments, issues
---------------------------

Post your comments in the github issues 

