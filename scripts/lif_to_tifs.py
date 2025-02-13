import os
import argparse
import numpy as np
import tifffile as tf
from readlif.reader import LifFile

# parse arguments
parser = argparse.ArgumentParser(description='Process a lif file.')
parser.add_argument('--input', type=str, help='path to the lif file')
args = parser.parse_args()

input_folder = args.input

lif_files = []
for file in os.listdir(input_folder):
    if file.endswith(".lif"):
        lif_files.append(file)





def scene_to_stack(scene):
    n_channels = scene.info['channels']
    array_list = []
    for i in range(n_channels):
        # get the array of the current scene
        frames = []
        for j in range(scene.nz):
            for t in range(scene.nt):    
                frame = scene.get_frame(t=t,c=i,z=j)
                # convert frame to numpy array
                frame = np.array(frame)
                frames.append(frame)
        frames = np.array(frames)
        array_list.append(frames)

    multichannel_stack = np.array(array_list)
    if len(multichannel_stack.shape) < 5:
         multichannel_stack = np.expand_dims(multichannel_stack, axis=0)
    else:
        pass    


    return multichannel_stack


def create_metadata(scene):
    scale_x = scene.info['scale_n'][1]
    scale_y = scene.info['scale_n'][2]
    
    # check if scale_z is defined in the dictionary
    if 3 in scene.info['scale_n']:
        scale_z = scene.info['scale_n'][3]
    else:
        scale_z = 1
    
    # get resolution in um
    x_res = 1 / scale_x 
    y_res = 1 / scale_y 
    z_res = 1 / scale_z 
    resolution = (x_res, y_res)
    metadata = {'spacing': z_res, 'unit': 'um'}
    return resolution, metadata

def save_image(image,res_meta,path):
    # save the image stack
    tf.imwrite(path, image,resolution = res_meta[0], metadata=res_meta[1], imagej=True) 

def process_scene(scene,path):
    multichannel_stack = scene_to_stack(scene)
    
    # create metadata
    res_meta = create_metadata(scene)
    position = scene.info['name']
    # replace "/" with "_" in position
    position = position.replace("/","_")
    # save the multichannel stack
    save_image(multichannel_stack,res_meta,path.split(".")[0] +"_{scene}.tif".format(scene=position))
    print("Processed {scene}".format(scene=position))

for lif_file in lif_files:
    
    if lif_file:
        
        path = os.path.join(input_folder, lif_file)
        # read the lif file
        lif = LifFile(path)
        # index all scenes in the lif file
        img_list = [i for i in lif.get_iter_image()]

        for scene in img_list:
            process_scene(scene,path)    

    else:
        print("No lif file found in the input folder.")
        exit()











