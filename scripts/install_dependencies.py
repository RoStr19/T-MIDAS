"""
mamba create -y -n tmidas-env python=3.9
mamba activate tmidas-env
python ./scripts/install_dependencies.py
"""




import subprocess

# List of dependencies to install
dependencies = [
    'numpy',
    'scikit-image',
    'tifffile',
    'pyclesperanto-prototype', 
    'Pillow',
    'napari-segment-blobs-and-things-with-membranes',
    'napari-simpleitk-image-processing',
    'pandas',
    'apoc', # GPU-accelerated pixel and object classification
    'aicsimageio', # for reading .czi files
    'opencv-python',  
    'readlif' # for reading .lif files
]

# Install each dependency using pip
for dependency in dependencies:
    subprocess.call(['pip', 'install', dependency])

# Additional installations for specific packages
subprocess.call(['pip', 'install', 'SimpleITK'])
subprocess.call(['pip', 'install', 'openslide-python']) # for reading .ndpi files 
subprocess.call(['pip', 'install', 'glob2'])
# mamba install -c conda-forge openslide
subprocess.call(['mamba', 'install', '-y', 'openslide','ocl-icd-system','pyopencl'])

print("All dependencies installed successfully.")
