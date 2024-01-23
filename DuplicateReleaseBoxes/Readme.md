## Script to duplicate release box in a separately generated .STL for import in Ansys FLUENT Meshing with specified filename

This section is comprised of 2 files.

### Duplicate stl with numpy-stl
[translate_stl.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/master/DuplicateReleaseBoxes/translate_stl.py) contains a function to translate and save the release box in a specified stl file (.stl) with a pre-determined grid spacing and initial location.

It should be noted that this function assumes that numpy-stl and shutil packages have been installed.

The function currently saves all duplicated boxes with the following form 'small-box=XX-YY.stl', where XX and YY correspond to the displacement in the x- and y- coordinate.

The current sample small-box-1-1.stl is a 0.2 x 0.2 x 0.2 m<sup>3</sup> box that serves as the template.

This is a two-step process:
1) Duplicate the box across a fixed grid with specified spacing in x-y directions (saved in 'small-box-copies' folder)
2) Define a range of inner spacing (box_exts) for which we should retain the boxes and copy these boxes over to another folder ('output_folder')


### Re-save STLs with Rhino to unscramble the filenames for Fluent Meshing
Upon generation of the duplicate boxes, numpy-stl package scrambles the stl name. 
We currently utilize Rhino to re-save the generated stl with filenames that are parseable by Fluent Meshing as-is.

[re-save-numpy-stl.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/master/DuplicateReleaseBoxes/re-save-numpy-stl.py) utilizes Rhino to resave the stl files in the original folder (location in the script; currently specified as 'output_folder' on Windows Desktop).


