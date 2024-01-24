## Script to create a scm to slice gridded locations at a specific z-height from a completed ANSYS FLUENT case file


### Create scm with known x- and y- extents for the domain
[generate-scm.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Extract_Scalar_onGrid/generate-scm.py) creates a gridded set of surfaces from a specified cut-plane which can then be used to extract the passive scalar concentrations.

x_min, x_max, y_min and y_max are determined by the spatial extents of the geometrical domain.

gap can be determined based on the desired gridded spacing, while this scm only works for a single height cut-plane. 


### Create scm with a python script to batch the use of first scm file for passive scalar concentration

[generate-scm.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Extract_Scalar_onGrid/generate-scm.py) creates a SCM with a repeated set of the following function calls in FLUENT.

Manually extract list of surfaces from the Fluent Case - This needs to be inserted into the script

We have to do the following:
1) Run an extra scm file which will load the ANSYS FLUENT case file
2) The scm file then loads the scm file into FLUENT and runs the (extract-ps)
4) The last step is to extract the surface-averaged passive scalar concentration at those surfaces into a text file
5) This can then be repeated for all case files in a folder
