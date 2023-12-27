import json
import os
import subprocess

def make_description_json(proj_name: str, bids_version: str, path=os.path.dirname(os.path.abspath(__name__))):
    """Makes necessary dataset_description.json as required via BIDS specification
    
    Parameters
    ----------
    proj_name: str
        Project name

    bids_version: str
        BIDS Version

    path: str, default: current path
        Path to output .json file
    """

    jdict = {"Name":f'{proj_name}',
             "BIDSVersion":f'{bids_version}'}

    with open("dataset_description.json", "w") as f:
        json.dump(jdict, f, ensure_ascii=False, indent=4)

def make_executable(engine: str or int, path=os.path.dirname(os.path.abspath(__name__))):
    """Create json file to execute this code in simple manner.
    
    Parameters
    ----------
    path: str, default: current path
        Path to output file
    
    engine: str or int
        Backend converter tool. Either 'dcm2bids' or 0 to execute dcm2bids or 'dcm2niix' or 1 to execute dcm2niix.
    """
    if engine == "dcm2niix" or engine == 1:
        dcm2niix_template = {"Engine": "<fill>", 
                    "Compression Level": "<fill>",
                    "Recompression? (Y/N)": "<fill>",
                    "BIDS Car? (Y/N)": "<fill>",
                    "Anonymize? (Y/N)": "<fill>",
                    "File name root": "<fill>",
                    }
        with open("pykevmri_executable.json", "w") as f:
            json.dump(dcm2niix_template, f, ensure_ascii=False, indent=4)

        subprocess.run(f'open {path}/pykevmri_executable.json -a "TextEdit"')

def execute_from_file():
    pass