from utils import *
from niixe import dcm2niix_convert

def convert(path: str, engine: str or int, **kwargs):
    """Convert DICOM files to NIFTI files in BIDS format following dcm2niix conventions, but with Python!

    Parameters
    ----------
    path: str
        Absolute path to the DICOM directory. 
    
    engine: str or int
        Backend converter tool. Either 'dcm2bids' or 0 to execute dcm2bids or 'dcm2niix' or 1 to execute dcm2niix.

    Keyword Arguments [dcm2bids]
    -----------------


    Keyword Arguments [dcm2niix]
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

    if engine == 'dcm2niix' or engine == 1:

        dcm2niix_convert(path, kwargs)

    elif engine == 'dcm2bids' or engine == 0:
        pass