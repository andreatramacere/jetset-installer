The following instructions explain how to install jetset from the binaries distributed on the git repo. It is advised to use python versions [3.8 - 3.9]. 

1) clone the repository

2) if you are using conda I suggest to create a new environment:  
   
   `conda create -n jetset python=3.8`
   
   and activate the environment: `conda activate jetset`

3) if you are using pip, the  creation of a new environment is optional, eg: 
    
   `pip install virtualenv`

    `virtualenv jetset`
   
    and activate the environment: `source jetset/bin/activate`
   

4) be sure that the following package is installed: pywget 
   - for conda: `conda install pywget`
   - for pip: `pip install pywget`
  
5) run the script, e.g for release 1.2.0rc8 run: 

   `python jetset_installer.py 1.2.0rc8`

Now jetset with all the dependencies is installed!
