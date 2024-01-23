# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2023. 

import rhinoscriptsyntax as rs
import os

def load_and_export_stl_with_spec_filename(filename):
    # Select the STL file to load
    #stl_file = rs.OpenFileName("Select STL file to load", "STL Files (*.stl)|*.stl||")
    #if not stl_file:
    #    return
    stl_file = filename
    #print(stl_file)

    # Get the filename without the path and extension
    # filename_without_extension = stl_file.split(rs.StringReverse(stl_file), "\\", 1)[0][0][:-4]
    
    # Define the export path using the same filename
    # export_path = rs.StringReverse(stl_file) + filename_without_extension + ".stl"
    export_path = stl_file

    # Load the STL file
    # mesh = rs.InsertFile(stl_file, import_mode=1)  # Import as a mesh
    mesh = rs.Command("_-Import " + stl_file + " _Enter")
    mesh_str = "_-Import " + stl_file + " _Enter"
    print(mesh_str) # Print to current file to console
    
    objs = rs.AllObjects()

    if mesh:
        # Export the mesh as an STL file with the same filename
        rs.SelectObject(objs)
        rs.Command("_-Export " + export_path + " _Enter", echo=False)
        rs.DeleteObject(objs)  # Delete the loaded mesh

        #print("STL mesh has been loaded and re-exported")
    #else:
        #print("Failed to load the STL file.")


if __name__ == "__main__":

    folder_path = "C:\Users\meepok\Desktop\output_folder"
    os.chdir(folder_path)
    for filename in sorted(os.listdir(folder_path)):
        if ".stl" in filename:
            file_path = os.path.join(folder_path, filename)
            load_and_export_stl_with_spec_filename(file_path)
    
