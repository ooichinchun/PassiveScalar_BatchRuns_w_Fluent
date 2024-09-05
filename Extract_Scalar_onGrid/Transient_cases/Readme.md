## Script to create a scm to slice gridded locations at a specific z-height from a completed ANSYS FLUENT case file
## This is a modified version for extracting the slices for transient FLUENT simulations


### Step 2: Create scm with a python script to batch the use of first scm file for passive scalar concentration from multiple data files in single transient simulation

##########################
#START PARAMETERS TO EDIT#
##########################

## Slice height can be modified from here
## This can be created by the .py file in Step 1

height_idx = '150'
input_ps_scm_file_path = '/data/ooicc/pcf-fengshan/completed-Table/scripts-ps-values-zw/export-ps-' + height_idx + 'cm.scm'

## Transient case simulation data are specified here
file_index = '08-16'

folder_path = '/data/ooicc/pcf-fengshan/completed-Grid/transient-case-files/transient-case-runs-' + file_index
overall_case_file = 'model-3-Scenario-Grid-base-' + file_index + '_ff_ps.cas.h5'

case_filename_prefix = 'model-3-Scenario-Grid-base-' + file_index + '-'

## Output scm file is created in directory where .py file is located.
output_scm_file_path = 'loop_data-' + file_index + '.scm'



Pre-work: 
1) Manually extract list of surfaces from the Fluent Case to insert into the script (copy into 'location_names' variable)
2) Put all case files into a single directory and provide path and prefix in the script ('folder_path', 'overall_case_file', 'case_filename_prefix' variables)
3) Input and output filenames are required to be defined. (e.g. 'height_idx', 'input_ps_scm_file_path', 'output_scm_file_path')

[loop_transient_case_data.py](https://github.com/ooichinchun/PassiveScalar_BatchRuns_w_Fluent/blob/main/Extract_Scalar_onGrid/Transient_cases/loop_transient_case_data.py) creates the scm file for a specified cut-plane which can then be used to extract the passive scalar concentrations.


### Instructions for Use

With the generated scripts from the above 2 steps, we can then batch the extraction of passive scalar concentration. 

The scm file (named as 'sample-cases.scm') in Step 2 can be launched from ANSYS FLUENT GUI and does the following:
1) Loop through the ANSYS FLUENT transient case files in the specified directory
2) Load the scm file from Step 1 into FLUENT and runs the (extract-ps)
3) Extract and save the surface-averaged passive scalar concentration at created surfaces into a text file (Manual extraction of surface names is required for one run first)
