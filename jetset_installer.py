import platform
import tarfile
import os
import sys
import subprocess
import argparse
import wget


def install(release):
    v=platform.python_version()
    py_v=v[0:3]
    
    base_url='https://github.com/andreatramacere/jetset/releases/download/%s'%release
    
    if platform.system()=='Darwin':
        system_str='macos-10.15'
    else:
        system_str='ubuntu-latest'
    

    conda_file='%s/conda-binary-%s-%s-py-%s.tar'%(base_url,release,system_str,py_v)
    pip_file='%s/pip-binary-%s-%s-py-%s.tar'%(base_url,release,system_str,py_v)
    
    use_conda=os.path.exists(os.path.join(sys.prefix, 'conda-meta'))
    if use_conda is True:
        print(conda_file)
        filename = wget.download(conda_file)
    else:
        print(pip_file)
        filename = wget.download(pip_file)

    print()
    filename=os.path.basename(filename)
    print(filename)

    file = tarfile.open(filename,'r:')
    print(file.getnames())

    file.extractall(path='tmp_jetset_install')
    file.close()
    if use_conda:
        cmd_lines=['conda install --yes --use-local tmp_jetset_install/*/jetset-*.tar.bz2']

        cmd_lines.append('conda update --yes  -c conda-forge -c astropy jetset')
    else:
        cmd_lines=['pip install tmp_jetset_install/*/jetset-*.whl']
    
    for cmd_line in cmd_lines:
        print(cmd_line)
        process = subprocess.run(cmd_line,shell=True, check=True)



def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('release', type=str, help='release name',default='1.2.0rc8' )
    args = parser.parse_args()    
    install(release=args.release)

if __name__=="__main__":
    main(sys.argv)