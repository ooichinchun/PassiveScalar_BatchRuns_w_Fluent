## Script to select random release location from a list of box zones in FLUENT ANSYS and create the SCM file to automate the simulation runs and passive scalar concentration extraction

This section contains only 1 file, but assumes the following 2 pre-requisites have been met:
1) Extracted list of zones in the Fluent Case (valid zones for release have been identified) - This should look similar to the sample [all-names-transpose.csv](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Select_RandLoc_Create_scm_for_Fluent/all-names-transpose.csv) example.
2) A first working Fluent case and data file has been created with pre-set desired passive scalar settings. The scm file only changes the source and patches the values to enable multiple runs to happen quickly.

### Duplicate stl with numpy-stl
[sample_values.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Select_RandLoc_Create_scm_for_Fluent/sample_values.py) samples from the possible list of locations with the Latin Hypercube Sampling algorithm and creates a Fluent SCM file to cycle through the simulations and extract the passive scalar concentrations.

It should be noted that this function assumes that the pyDOE package has been installed and a list of all zones in FLUENT are provided.

The function currently saves the selected samples with their zone IDs in the 'zone_name_n_170.csv' file, along with their x,y coordinates.

num_samples needs to be modified to generate the number of samples required. Note that this is not the final actual number as there is a post-LHS filtering step to ensure the sampled locations are valid locations within the geometry.

This is a two-step process:
1) Generate list of x,y locations from LHS
2) Retain only sampled locations that are present in the list of locations specified in 'all-names-transpose.csv' (Note that the check assumes a gridded list of locations currently)
3) The filename specified in <u>prev_zone = 'small-box-01-05:270313'</u> needs to be changed to some random (but valid) zone name for the very first run. This zone is needed as a filler to set the UDS source to 0 for the first run.
4) The list of zones in the scm needs to be updated.
5) The save directories for the Vol-avg Passive Scalar value and the FLUENT case and data file need to be updated as desired. (Search for '.txt' and '.cas.h5')



### Using the scm file
The generated scm file will do the following:
1) Define the user-defined scalar source term for the zone in the previous run to 0
2) Define the user-defined scalar source term for the new zone ID to be 1 (to simulate release)
3) Patch the values in all zones to be 0 as initialization
4) Patch the value in the source zone to be 1
5) Solve to pre-specified convergence criteria (usually set at 1e-10) with 50k iterations
6) Extract the volume-averaged user-defined scalar concentration at all the pre-specified zones of interest (can re-use the list in all-names-transpose.csv) and save it as 'vol-avg-grid-X_STR-Y_STR.txt'
7) Save the new case and data file with solved passive scalar concentration as 'model-3-Scenario-Grid-base-X_STR-Y_STR.cas.h5'

