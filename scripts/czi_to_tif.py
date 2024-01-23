import os
import argparse
from aicsimageio import AICSImage
from aicsimageio.writers import OmeTiffWriter


# parse arguments
parser = argparse.ArgumentParser(description='Process czi files.')
parser.add_argument('--input', type=str, help='path to the czi files')
args = parser.parse_args()

folder = args.input

def czi_scenes_to_tifs(filepath):
    # test using AICSImageIO
    aics_img = AICSImage(filepath, reconstruct_mosaic=True)
    # export each scene as tif
    for i in aics_img.scenes:
        aics_img.set_scene(i)
        print("Exporting " + str(i) + " with shape "+ str(aics_img.data.shape)+ " and dim order " + str(aics_img.dims.order) + " to ome.tiff.")
        OmeTiffWriter.save(aics_img.data, 
                           filepath.replace(".czi", f"_{i}.ome.tiff"), 
                           physical_pixel_sizes=aics_img.physical_pixel_sizes, 
                           dim_order=aics_img.dims.order, 
                           channel_names=aics_img.channel_names,
                           # list of channel colors RBG hexadecimals
                           channel_colors=[0xFF0000,0x00FF00,0x0000FF]
                           )
        # #aics_img.save(filepath.replace(".czi", f"_{i}.ome.tiff"), select_scenes=[i]) # bug with colors?

for file in os.listdir(folder):
    if file.endswith(".czi"):
        czi_scenes_to_tifs(os.path.join(folder, file))
