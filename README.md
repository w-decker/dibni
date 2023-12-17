# PyKevMRI
Merging [`dcm2niix`](https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage) with Python neuroimaging analysis workflow. 

# Documentation
This code makes use of a single function, `convert()`, which takes arguments similar to the flags used in the command line tool, `dcm2niix`. There is also some additional "behind the scenes" functionality, which makes DICOM to NIFTI conversion smoother for novice users.

To execute in a workflow, simply import the module, `from pykevmri import convert`. `convert`, takes a single parameter, `path=`. Here, you must specify the absolute path to a directory containing DICOM files or compressed `.tgz` files. You may also provide optional keyword arguments too to further customize your workflow.

# Important
The following updates are expected to be implemented shortly:
1. Choice of "engine": `dcm2niix`, [`dcm2bids`](https://unfmontreal.github.io/Dcm2Bids/3.1.1/) or [`heudiconv`](https://github.com/nipy/heudiconv). Each has slightly different functionality and thus, seperate workflows for each will be created.
2. Dynamic access either with direct interfacing between GitHub (similar to R's `devtools:install_github`) and the user or PyPi. 
