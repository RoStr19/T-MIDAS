import os
import argparse
from aicsimageio import AICSImage
from aicsimageio.writers import OmeTiffWriter
import numpy as np
import cv2
from PIL import Image

# parse arguments
parser = argparse.ArgumentParser(description='Process czi files.')
parser.add_argument('--input', type=str, help='path to the czi files')
args = parser.parse_args()

folder = args.input

scale_factor = 0.5

def czi_scenes_to_tifs(filepath):

    aics_img = AICSImage(filepath, reconstruct_mosaic=True)    

    for i in aics_img.scenes:
        aics_img.set_scene(i)
        img = aics_img.get_image_data("YXS", Z=0, T=0, C=0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resized_img = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor)
        Image.fromarray(resized_img).save(filepath.replace(".czi", f"_{i}.tiff"), 
                                    dpi = (scale_factor*25400.0/aics_img.physical_pixel_sizes[2], scale_factor*25400.0/aics_img.physical_pixel_sizes[1]),
                                    compression="tiff_deflate")


for file in os.listdir(folder):
    if file.endswith(".czi"):
        czi_scenes_to_tifs(os.path.join(folder, file))
