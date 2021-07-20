# Instructions
The following instructions explain how to install jetset from the binaries distributed on the git repo. It is advised to use python versions [3.8 - 3.9]. 

## Clone the repository

1) clone the repository:

   `git clone https://github.com/andreatramacere/jetset-installer.git`
   
   `cd jetset-installer/`

## Prepare virtual env (optional)
2) if you are using conda I suggest to create a new environment:  
   
   `conda create -n jetset python=3.8`
   
   and activate the environment: `conda activate jetset`

3) if you are using pip, the  creation of a new environment is optional, eg: 
    
   `pip install virtualenv`

    `python -m venv jetset`
   
    and activate the environment: `source jetset/bin/activate`
   
## Install wget

4) be sure that the following package is installed: wget 
   - for conda: `conda install wget`
   - for pip: `pip install wget`

## JetSeT installation

5) run the script, e.g for release 1.2.0rc8 run: 

   `python jetset_installer.py 1.2.0rc8`

**run the code and the example in a different directory**

Now jetset with all the dependencies is installed!
