import sys
import os
import subprocess

def check_dcm2niix():
    """Checks if dcm2niix is installed"""
    # check OS
    syst = None
    dcm2niix_exist = None
    if sys.platform == 'linux' or sys.platform == 'linux2':
        syst = 'l' # linux
    elif sys.platform == 'darwin':
        syst = 'm' # mac OS
        if os.path.exists('/opt/homebrew/bin/dcm2niix'):
            dcm2niix_exist = True
    elif sys.platform == 'win31':
        syst = 'w'
        if os.path.exists("C:\\Program Files\\dcm2niix\\dcm2niix.exe"):
            dcm2niix_exist = True

    return(dcm2niix_exist)
def check_gz(path):
    """Checks if all individual files are uncompressed"""
    # unzip file
    if path.split[-1] == '.tgz':
        subprocess.run(f'tar -kxvzf {path} -C {os.path.dirname(path)}', shell=True, check=True, text=True)
    else:
        pass

def get_kwargs(kwargs: dict):
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
    expect = {
                "comp_level": 1,
                "recomp": True,
                "bidscar": True,
                "anon": True,
                "fname_root": "sub", 
                "out": f"Users/{os.getlogin()}",
                "single_file": False
              }
    
    for i in kwargs

    out = []
    for i in kwargs:
        out.append(kwargs.get(i))