## Script to create a scm to slice gridded locations at a specific z-height from a completed ANSYS FLUENT case file


### Step 1: Create scm with known x- and y- extents for the domain
[generate-scm.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Extract_Scalar_onGrid/generate-scm.py) creates a gridded set of surfaces from a specified cut-plane which can then be used to extract the passive scalar concentrations.

x_min, x_max, y_min and y_max are determined by the spatial extents of the geometrical domain.

gap can be determined based on the desired gridded spacing.

The current scm template only works for a cut-plane at a single height but this can be easily adjusted.


### Step 2: Create scm with a python script to batch the use of first scm file for passive scalar concentration from multiple case files

Pre-work: 
1) Manually extract list of surfaces from the Fluent Case to insert into the script
2) Put all case files into a single directory and provide path in the script
3) Input and output filenames are required to be defined.


[generate-scm.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Extract_Scalar_onGrid/generate-scm.py) creates a SCM with repeated calls of the necessary commands in FLUENT for different cases in the directory


### Instructions for Use

With the generated scripts from the above 2 steps, we can then batch the extraction of passive scalar concentration. 

The scm file in Step 2 can be launched from ANSYS FLUENT GUI and does the following:
1) Loop through the ANSYS FLUENT case files in the specified directory
2) Load the scm file from Step 1 into FLUENT and runs the (extract-ps)
3) Extract and save the surface-averaged passive scalar concentration at created surfaces into a text file (Manual extraction of surface names is required for one run first)
