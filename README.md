# DIBNI
Converting DICOM files to BIDS compliant NIFTI files. This code merges and executes command line tools like [`dcm2niix`](https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage), [`dcm2bids`](https://unfmontreal.github.io/Dcm2Bids/3.1.1/) and (forthcoming) [`heudiconv`](https://heudiconv.readthedocs.io/en/latest/usage.html). 

# Documentation
This code makes use of a single function, `convert()`, which takes arguments similar to the flags used in the command line tools. If you wish to forgo the Python interface when laboring over file conversion, you may also convert files by filling in a template **.json** file, which is created using the function `make_executable_json()` and implemented using `execute_from_file()`. The json file looks something like below:
```json
{
    "BIDSVersion": "<fill>"
}
```
where `<fill>` indicates a position which must be provided by the user. This is then read into the program as a `dict`. This avoids some potential syntactic confusion by novice users.

To execute in a workflow, simply import the module, `from pykevmri import convert`. `convert`, takes a required parameter, `path=` and `engine=`. Here, you must specify the absolute path to a directory containing DICOM files or compressed `.tgz` files and the engine (dcm2niix, dcm2bids, heudiconv). You may also provide optional keyword arguments too to further customize your workflow. These optional keywords are different depending on the engine used. Documentation coming soon. 

# Important
The following updates are expected to be implemented shortly:
1. Choice of "engine": `dcm2niix`, [`dcm2bids`](https://unfmontreal.github.io/Dcm2Bids/3.1.1/) or [`heudiconv`](https://github.com/nipy/heudiconv). Each has slightly different functionality and thus, seperate workflows for each will be created.
2. Dynamic access either with direct interfacing between GitHub (similar to R's `devtools:install_github`) and the user or PyPi. 
