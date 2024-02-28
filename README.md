![T-MIDAS Logo](https://github.com/MercaderLabAnatomy/T-MIDAS/assets/99955854/aada2d33-f5f7-4395-bf36-c0466b304d0d) 
# Tissue Microscopy Image Data Analysis Suite


T-MIDAS was created with a focus on the reproducibility of typical batch processing workflows for biological tissue microscopy data. 
- Executable with a simple text-based user interface
- Runs on any low-grade workstation with a single GPU
  
- Supported imaging modalities:
  - Confocal microscopy images
  - Slidescanner images
  - Multicolor and brightfield
    
- Features include:
  - Image Format Conversion (proprietary to open)
  - Image Preprocessing
  - Image Segmentation
  - Image Segmentation Validation
  - Region-of-interest (ROI) Analyses
    
- Quick and Easy Installation

## Text-based User Interface
![image](https://github.com/MercaderLabAnatomy/T-MIDAS/assets/99955854/ef71315b-726d-4a2f-9546-d326aba513dd)


## List of Features for Automated Batch Processing

![image](https://github.com/MercaderLabAnatomy/T-MIDAS/assets/99955854/8f455c1a-e87f-41bd-bfde-3909dce2ed22)





## WIP
- Workflow logging
- Plug & Play DGMs for Transfer Learning (PyTorch framework)
- Lightsheet data
- Time series data

## Installation
```
mamba create -y -n tmidas-env python=3.9
mamba activate tmidas-env
python ./scripts/install_dependencies.py
```
