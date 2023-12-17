import glob
import os
import sys
from utils import check_dcm2niix, check_gz, get_kwargs

def convert(path: str, **kwargs):
    """Convert DICOM files to NIFTI files in BIDS format following dcm2niix conventions, but with Python!

    Parameters
    ----------
    path: str
        Absolute path to the DICOM directory. 

    Keyword Arguments
    -----------------
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

    # check that dcm2niix is installed
    check_dcm2niix()

    # check that all files are unzipped
    dir = os.listdir(path)
    [check_gz(i) for i in dir]

    # convert from DICOM to NIFTI
    for i in dir:

            

            


