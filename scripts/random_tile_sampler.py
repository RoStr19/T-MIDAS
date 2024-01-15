import numpy as np
import random
import argparse
import tifffile as tf
import os

def load_tiff_image(path):
    return tf.imread(path)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Sample random tiles from a tiff image.')
    parser.add_argument('--input', type=str, help='Folder containing the .tif images.')
    parser.add_argument('--tile_diagonal', type=int, help='Enter the tile diagonal in pixels.')
    # parser.add_argument('--num_tiles', type=int, help='Enter the number of tiles to sample.')
    return parser.parse_args()

# path = "/mnt/disk2/Asli/Experiments/Experiment01/7-ki67 - 2022-11-16 17.35.20.tif"

def is_multichannel(image):
    return len(image.shape) == 3


# image = load_tiff_image(path)
# is_multichannel(image)

# the following function creates a grid based on image xy shape and tile diagonal and then randomly samples 20% of the available tiles
def sample_tiles_random(image, tile_diagonal, subset_percentage=20):
    tiles = []
    height, width = image.shape[1], image.shape[2]
    # print("image shape: ("+str(height)+","+str(width)+")\n")
    tile_size = int(np.sqrt(2) * tile_diagonal)  # Calculate the tile size
    
    step_h = int(tile_size)  # Set step sizes based on the tile size
    step_w = int(tile_size)
    
    possible_positions = []  # Store all possible tile positions
    
    for i in range(0, height - tile_size + 1, step_h):
        for j in range(0, width - tile_size + 1, step_w):
            possible_positions.append((i, j))  # Collect all possible tile positions
    
    num_subset_tiles = int(len(possible_positions) * (subset_percentage / 100))  # Calculate number of tiles for subset
    selected_positions = random.sample(possible_positions, num_subset_tiles)  # Randomly select non-overlapping positions
    
    if is_multichannel(image):
        for pos in selected_positions:
            i, j = pos
            tile = image[:,i:i+tile_size, j:j+tile_size]
            tiles.append(tile)
    else:
        for pos in selected_positions:
            i, j = pos
            tile = image[i:i+tile_size, j:j+tile_size]
            tiles.append(tile)
    
    return tiles

# test = sample_tiles_random(image,724)
# test[1]

def save_tiles(tiles, path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, tile in enumerate(tiles, start=1):  # Start enumeration at 1
        filename = os.path.basename(path)
        filename = filename.split('.')[0] + '_tile_' + str(i).zfill(2) + '.tif'
        save_path = os.path.join(output_dir, filename)
        tf.imwrite(save_path, tile)



def process_image(path, tile_diagonal, output_dir):
    image = load_tiff_image(path)
    tiles = sample_tiles_random(image, tile_diagonal)
    save_tiles(tiles, path, output_dir)

def main():
    args = parse_arguments()
    output_dir = os.path.join(args.input, 'random_tiles')

    for filename in os.listdir(args.input):
        if filename.endswith(".tif"):
            path = os.path.join(args.input, filename)
            process_image(path, args.tile_diagonal, output_dir)
        else:
            continue

if __name__ == "__main__":
    main()
