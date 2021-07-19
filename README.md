1) clone the repository

2) (suggested)if you are using conda create a new environment eg:  `conda create -n jetset python=3.8`
   
   and activate the environment: `conda activate jetset`

3) (optional)if you are using pip creante a new environment eg: 
    
   `pip install virtualenv`

    `virtualenv jetset`
   
    and activate the environment: `source jetset/bin/activate`
   

4) be sure that the following package is installed: pywget 
   - for conda: `conda install pywget`
   - for pip: `pip install pywget`
  
5) run the script, e.g for release 1.2.0rc8 run: 
   `python jetset-installer.py 1.2.0rc8`

Now jetset with all the dependencies is installed!