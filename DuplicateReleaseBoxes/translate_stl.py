# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2023. 

# !pip install numpy-stl

import numpy as np
from stl import mesh
import os
import shutil

# First step duplicates stl file in a fixed grid
# This replicates the box in a grid with 0.5 m spacing in both x- and y- directions

template_stl = 'small-box-1-1.stl'
# First generated file is small-box-01-01.stl at the exact same location, but placed in the new folder

# Folder path containing the files for full uniform grid (47 x 23 boxes)
folder_path = "small-box-copies"
os.makedirs(folder_path, exist_ok=True)

# Additional +1 is to compensate for range being non-inclusive of input parameter in upper bound
nx_max = 47 + 1
ny_max = 23 + 1
grid_spacing = 0.5
pad = 2 # For ease of naming and referencing

# Displacement amount (left-right is x-axis; up-down is y-axis)
t_up = np.array([0, grid_spacing, 0])
t_right = np.array([grid_spacing, 0, 0])

for i in range(1,nx_max):

  stl_data = mesh.Mesh.from_file(template_stl)
  t_right_cur = t_right*(i-1)
  stl_data.translate(t_right_cur)

  filename = 'small-box-' + str(i).zfill(pad) + '-01.stl'
  cur_file = os.path.join(folder_path, filename)

  stl_data.save(cur_file)

  for j in range(2,ny_max): #Start from 2 as the first row is already created

    stl_data.translate(t_up)
    filename = 'small-box-' + str(i).zfill(pad) + '-' + str(j).zfill(pad) + '.stl'
    cur_file = os.path.join(folder_path, filename)

    stl_data.save(cur_file)

#print(stl_data.name)


# Create list of x- and y- extents if the grid has variable missing locations

box_exts = {}
box_exts['1'] = [3,13]
box_exts['2'] = [3,13]
box_exts['3'] = [3,13]
box_exts['4'] = [3,13]
box_exts['5'] = [3,17]
box_exts['6'] = [1,17]
box_exts['6'] = [1,17]
box_exts['6'] = [1,17]
box_exts['7'] = [1,17]
box_exts['8'] = [1,17]
box_exts['9'] = [1,17]
box_exts['10'] = [1,17]
box_exts['11'] = [9,17]
box_exts['12'] = [9,17]
box_exts['13'] = [3,17]
box_exts['14'] = [3,17]
box_exts['15'] = [3,17]
box_exts['16'] = [3,23]
box_exts['17'] = [3,23]
box_exts['18'] = [3,23]
box_exts['19'] = [9,23]
box_exts['20'] = [9,23]
box_exts['21'] = [9,23]
box_exts['22'] = [9,23]
box_exts['23'] = [9,23]
box_exts['24'] = [9,23]
box_exts['25'] = [9,23]
box_exts['26'] = [9,23]
box_exts['27'] = [9,23]
box_exts['28'] = [9,17]
box_exts['29'] = [9,17]
box_exts['30'] = [9,17]
box_exts['31'] = [9,17]
box_exts['32'] = [9,17]
box_exts['33'] = [1,17]
box_exts['34'] = [1,17]
box_exts['35'] = [1,17]
box_exts['36'] = [1,17]
box_exts['37'] = [1,17]
box_exts['38'] = [1,17]
box_exts['39'] = [1,16]
box_exts['40'] = [1,16]
box_exts['41'] = [1,16]
box_exts['42'] = [1,16]
box_exts['43'] = [1,16]
box_exts['44'] = [1,16]
box_exts['45'] = [1,16]
box_exts['46'] = [1,16]
box_exts['47'] = [1,16]


# Format for the specific number you want to match for referencing
#target_number = "01-01"

# Create a directory to store the matching files
output_folder = "output_folder"
os.makedirs(output_folder, exist_ok=True)

for i in range(1,48):
  for j in range(box_exts[str(i)][0],box_exts[str(i)][1]+1):
    target_number = str(i).zfill(pad) + '-' + str(j).zfill(pad)

    # Loop through the files in the folder
    for filename in sorted(os.listdir(folder_path)):
      #if filename.endswith(".stl"):
	  
      # Check if the target number is in the file name
      if target_number in filename:
        source_file = os.path.join(folder_path, filename)
        destination_file = os.path.join(output_folder, filename)

        # Copy the matching file to the output folder
        shutil.copy2(source_file, destination_file)
        print(f"Copied: {filename} to {output_folder}")

print("Copy process complete.")

## Make sure to run Rhino Python script to load and save over stl in the current folder again to overwrite numpy-stl naming watermark



''' Full list of additional stl boxes that were removed as they are too close to pillars or walls

06-11
06-12
07-11
07-12
12-11
12-12
13-08
13-11
13-12
14-08
16-18
17-08
17-18
18-08
18-18
18-11
18-12
19-18
20-18
21-18
22-18
23-11
23-12
23-18
24-11
24-12
24-18
25-18
26-18
27-18
30-11
30-12
36-01
36-02
36-11
36-12
37-11
37-12
42-11
42-12
43-11
43-12

'''

