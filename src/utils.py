import sys
import os
import subprocess
import numpy as np
from itertools import chain
import json

def tgzunzip(path):
    dir = os.listdir(path)
    [check_gz(i) for i in dir]
    r = (f'     ---------------------\n \
        Checked for .tgz files\n \
        ---------------------')
    return (print(r))


def check_engine(engine):
    """Checks if engine is installed"""
    # check OS
    syst = None
    if sys.platform == 'linux' or sys.platform == 'linux2':
        syst = 'l' # linux
    elif sys.platform == 'darwin':
        syst = 'm' # mac OS
    elif sys.platform == 'win31':
        syst = 'w'

    if engine == 1:
        engine = 'dcm2niix'
    elif engine == 0:
        engine = 'dcm2bids'

    if syst == 'm' and os.path.exists(f'/opt/homebrew/bin/{engine}'):
        dcm2niix_exist = True
    elif syst == 'l':
        dcm2niix_exist = print(f'You are using Linux. Please ensure {engine} is properly installed.')
    elif syst == 'w':
        dcm2niix_exist = print(f'Windows functionality does not yet exist.')

    return(dcm2niix_exist)

def check_gz(path):
    """Checks if all individual files are uncompressed. If compressed, will uncompress in same directory."""
    # unzip file
    if path.split('.')[-1] == '.tgz':
        subprocess.run(f'tar -kxvzf {path} -C {os.path.dirname(path)}', shell=True, check=True, text=True)
    else:
        pass

def get_kwargs(engine, kwargs: dict):
    """Parse keyword args and return list of dcm2niix flags
    
    Input specifity
    ---------------
    comp_level: int
        Compression level. 1=fast, 9=slow

    recomp: bool
        re/compress nifti
    
    bidscar: bool
        Execute BIDS sidecar

    anon: bool
        Anonymize BIDS data

    fname_root: str
        File name root.
        Example: root='sub'
        Output: sub-001.nii

    out: str
        Output directory. Program will default to same directory

    single_file: list: [bool, path]
        If you wish to convert a single file, provide a list as the arg for this parameter in which index [0] is bool
        and index[1] is the specific file you wish to convert
    """

    if kwargs.get('fname_root') is None:
         val = None
    else:
         val = kwargs.get('fname_root') + '%a'

    if kwargs.get('single_file_path') is None:
        val1 = None
    else:
        val1 = kwargs.get('single_file_path')

    if kwargs.get("comp_level") is None:
        val2 = None
    else:
        val2 = kwargs.get("comp_level")

    expect = {
                "comp_level": val2,
                "recomp": '-z',
                "bidscar": '-b',
                "anon": '-ba',
                "fname_root":'-f', 
                "single_file": '-s',
                "single_file_path": val1,
                "out": '-o'
              }

    if kwargs.get("bidscar") is True:
        kwargs["bidscar"] = "y"

    if kwargs.get("anon") is True:
        kwargs["anon"] = "y"

    # compare keys
    got = list(set(expect.keys()).intersection(kwargs))

    out = []
    for i in got:
        out.append(expect.get(i))
        out.append(kwargs.get(i))

    for i in out:
        if type(i) == bool:
            out.remove(i)
        else:
            pass

    out = ' '.join(map(str, out))
    return(out)


    

        
