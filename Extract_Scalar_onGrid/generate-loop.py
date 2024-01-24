# Script written by Ooi Chin Chun
# Institute of High Performance Computing, Singapore
# Copyright (c) 2023. 

import re
import os

# scm filename is of format 'export-ps-height-cm.scm'
# make sure file path for scm in duplicate_text is updated
# make sure location_names is correctly extracted for any new geometry with new extents
# folder_path and heights need to be updated for new problems
# if statements and output filenames need to be updated for new problems

def duplicate_text(scm_fn, case_file_path, output_fn, loc_names):
  lines = '''(ti-menu-load-string " /file/read-case-data FILE_PATH ok")
(ti-menu-load-string " /file/read-macros /data/ooicc/pcf-fengshan/completed-Table/scripts-ps-values-zw/SCM_FILENAME")
(ti-menu-load-string " (extract-ps)")
(ti-menu-load-string " /report/surface-integrals/area-weighted-avg START small-box-01-03:270343 END () uds-0 yes OUTPUT_FILENAME")'''.split('\n')

  lines = [line + '\n' for line in lines]
  lines = [re.sub('SCM_FILENAME', scm_fn, line) for line in lines]
  lines = [re.sub('OUTPUT_FILENAME', output_fn, line) for line in lines]	
  lines = [re.sub('FILE_PATH', str(case_file_path), line) for line in lines]
  lines = [re.sub('START small-box-01-03:270343 END', loc_names, line) for line in lines]

  return lines

def write_lines(height, file_path, output_fn, location_names):

  scm_filename = 'export-ps-' + str(height) + 'cm.scm'
  #lines = duplicate_text(x_str, y_str, scm_filename, file_path, output_fn, location_names)
  lines = duplicate_text(scm_filename, file_path, output_fn, location_names)
  file.writelines(lines)
  file.writelines('\n')

  return 0


location_names = 'x10y10z1 x10y11z1 x10y12z1 x10y13z1 x10y14z1 x10y15z1 x10y16z1 x10y17z1 x10y18z1 x10y19z1 x10y1z1 x10y2z1 x10y3z1 x10y4z1 x10y5z1 x10y6z1 x10y7z1 x10y8z1 x10y9z1 x11y10z1 x11y11z1 x11y12z1 x11y13z1 x11y14z1 x11y15z1 x11y16z1 x11y17z1 x11y18z1 x11y19z1 x11y9z1 x12y10z1 x12y11z1 x12y12z1 x12y13z1 x12y14z1 x12y15z1 x12y16z1 x12y17z1 x12y18z1 x12y19z1 x12y3z1 x12y4z1 x12y5z1 x12y6z1 x12y7z1 x12y8z1 x12y9z1 x13y10z1 x13y11z1 x13y12z1 x13y13z1 x13y14z1 x13y15z1 x13y16z1 x13y17z1 x13y18z1 x13y19z1 x13y3z1 x13y4z1 x13y5z1 x13y6z1 x13y7z1 x13y8z1 x13y9z1 x14y10z1 x14y11z1 x14y12z1 x14y13z1 x14y14z1 x14y15z1 x14y16z1 x14y17z1 x14y18z1 x14y19z1 x14y3z1 x14y4z1 x14y5z1 x14y6z1 x14y7z1 x14y8z1 x14y9z1 x15y10z1 x15y11z1 x15y12z1 x15y13z1 x15y14z1 x15y15z1 x15y16z1 x15y17z1 x15y18z1 x15y19z1 x15y20z1 x15y21z1 x15y22z1 x15y23z1 x15y24z1 x15y3z1 x15y4z1 x15y5z1 x15y6z1 x15y7z1 x15y8z1 x15y9z1 x16y10z1 x16y11z1 x16y12z1 x16y13z1 x16y14z1 x16y15z1 x16y16z1 x16y17z1 x16y18z1 x16y19z1 x16y20z1 x16y21z1 x16y22z1 x16y23z1 x16y24z1 x16y3z1 x16y4z1 x16y5z1 x16y6z1 x16y7z1 x16y8z1 x16y9z1 x17y10z1 x17y11z1 x17y12z1 x17y13z1 x17y14z1 x17y15z1 x17y16z1 x17y17z1 x17y18z1 x17y19z1 x17y20z1 x17y21z1 x17y22z1 x17y23z1 x17y24z1 x17y3z1 x17y4z1 x17y5z1 x17y6z1 x17y7z1 x17y8z1 x17y9z1 x18y10z1 x18y11z1 x18y12z1 x18y13z1 x18y14z1 x18y15z1 x18y16z1 x18y17z1 x18y18z1 x18y19z1 x18y20z1 x18y21z1 x18y22z1 x18y23z1 x18y24z1 x18y3z1 x18y4z1 x18y5z1 x18y6z1 x18y7z1 x18y8z1 x18y9z1 x19y10z1 x19y11z1 x19y12z1 x19y13z1 x19y14z1 x19y15z1 x19y16z1 x19y17z1 x19y18z1 x19y19z1 x19y20z1 x19y21z1 x19y22z1 x19y23z1 x19y24z1 x19y9z1 x1y10z1 x1y11z1 x1y12z1 x1y13z1 x1y14z1 x1y3z1 x1y4z1 x1y5z1 x1y6z1 x1y7z1 x1y8z1 x1y9z1 x20y10z1 x20y11z1 x20y12z1 x20y13z1 x20y14z1 x20y15z1 x20y16z1 x20y17z1 x20y18z1 x20y19z1 x20y20z1 x20y21z1 x20y22z1 x20y23z1 x20y24z1 x20y9z1 x21y10z1 x21y11z1 x21y12z1 x21y13z1 x21y14z1 x21y15z1 x21y16z1 x21y17z1 x21y18z1 x21y19z1 x21y20z1 x21y21z1 x21y22z1 x21y23z1 x21y24z1 x21y9z1 x22y10z1 x22y11z1 x22y12z1 x22y13z1 x22y14z1 x22y15z1 x22y16z1 x22y17z1 x22y18z1 x22y19z1 x22y20z1 x22y21z1 x22y22z1 x22y23z1 x22y24z1 x22y9z1 x23y10z1 x23y11z1 x23y12z1 x23y13z1 x23y14z1 x23y15z1 x23y16z1 x23y17z1 x23y18z1 x23y19z1 x23y20z1 x23y21z1 x23y22z1 x23y23z1 x23y24z1 x23y9z1 x24y10z1 x24y11z1 x24y12z1 x24y13z1 x24y14z1 x24y15z1 x24y16z1 x24y17z1 x24y18z1 x24y19z1 x24y20z1 x24y21z1 x24y22z1 x24y23z1 x24y24z1 x24y9z1 x25y10z1 x25y11z1 x25y12z1 x25y13z1 x25y14z1 x25y15z1 x25y16z1 x25y17z1 x25y18z1 x25y19z1 x25y20z1 x25y21z1 x25y22z1 x25y23z1 x25y24z1 x25y9z1 x26y10z1 x26y11z1 x26y12z1 x26y13z1 x26y14z1 x26y15z1 x26y16z1 x26y17z1 x26y18z1 x26y19z1 x26y20z1 x26y21z1 x26y22z1 x26y23z1 x26y24z1 x26y9z1 x27y10z1 x27y11z1 x27y12z1 x27y13z1 x27y14z1 x27y15z1 x27y16z1 x27y17z1 x27y18z1 x27y19z1 x27y20z1 x27y21z1 x27y22z1 x27y23z1 x27y24z1 x27y9z1 x28y10z1 x28y11z1 x28y12z1 x28y13z1 x28y14z1 x28y15z1 x28y16z1 x28y17z1 x28y18z1 x28y19z1 x28y9z1 x29y10z1 x29y11z1 x29y12z1 x29y13z1 x29y14z1 x29y15z1 x29y16z1 x29y17z1 x29y18z1 x29y19z1 x29y9z1 x2y10z1 x2y11z1 x2y12z1 x2y13z1 x2y14z1 x2y3z1 x2y4z1 x2y5z1 x2y6z1 x2y7z1 x2y8z1 x2y9z1 x30y10z1 x30y11z1 x30y12z1 x30y13z1 x30y14z1 x30y15z1 x30y16z1 x30y17z1 x30y18z1 x30y19z1 x30y9z1 x31y10z1 x31y11z1 x31y12z1 x31y13z1 x31y14z1 x31y15z1 x31y16z1 x31y17z1 x31y18z1 x31y19z1 x31y9z1 x32y10z1 x32y11z1 x32y12z1 x32y13z1 x32y14z1 x32y15z1 x32y16z1 x32y17z1 x32y18z1 x32y19z1 x32y1z1 x32y2z1 x32y3z1 x32y4z1 x32y5z1 x32y6z1 x32y7z1 x32y8z1 x32y9z1 x33y10z1 x33y11z1 x33y12z1 x33y13z1 x33y14z1 x33y15z1 x33y16z1 x33y17z1 x33y18z1 x33y19z1 x33y1z1 x33y2z1 x33y3z1 x33y4z1 x33y5z1 x33y6z1 x33y7z1 x33y8z1 x33y9z1 x34y10z1 x34y11z1 x34y12z1 x34y13z1 x34y14z1 x34y15z1 x34y16z1 x34y17z1 x34y18z1 x34y19z1 x34y1z1 x34y2z1 x34y3z1 x34y4z1 x34y5z1 x34y6z1 x34y7z1 x34y8z1 x34y9z1 x35y10z1 x35y11z1 x35y12z1 x35y13z1 x35y14z1 x35y15z1 x35y16z1 x35y17z1 x35y18z1 x35y19z1 x35y1z1 x35y2z1 x35y3z1 x35y4z1 x35y5z1 x35y6z1 x35y7z1 x35y8z1 x35y9z1 x36y10z1 x36y11z1 x36y12z1 x36y13z1 x36y14z1 x36y15z1 x36y16z1 x36y17z1 x36y18z1 x36y19z1 x36y1z1 x36y2z1 x36y3z1 x36y4z1 x36y5z1 x36y6z1 x36y7z1 x36y8z1 x36y9z1 x37y10z1 x37y11z1 x37y12z1 x37y13z1 x37y14z1 x37y15z1 x37y16z1 x37y17z1 x37y18z1 x37y19z1 x37y1z1 x37y2z1 x37y3z1 x37y4z1 x37y5z1 x37y6z1 x37y7z1 x37y8z1 x37y9z1 x38y10z1 x38y11z1 x38y12z1 x38y13z1 x38y14z1 x38y15z1 x38y16z1 x38y17z1 x38y18z1 x38y19z1 x38y1z1 x38y2z1 x38y3z1 x38y4z1 x38y5z1 x38y6z1 x38y7z1 x38y8z1 x38y9z1 x39y10z1 x39y11z1 x39y12z1 x39y13z1 x39y14z1 x39y15z1 x39y16z1 x39y17z1 x39y1z1 x39y2z1 x39y3z1 x39y4z1 x39y5z1 x39y6z1 x39y7z1 x39y8z1 x39y9z1 x3y10z1 x3y11z1 x3y12z1 x3y13z1 x3y14z1 x3y3z1 x3y4z1 x3y5z1 x3y6z1 x3y7z1 x3y8z1 x3y9z1 x40y10z1 x40y11z1 x40y12z1 x40y13z1 x40y14z1 x40y15z1 x40y16z1 x40y17z1 x40y1z1 x40y2z1 x40y3z1 x40y4z1 x40y5z1 x40y6z1 x40y7z1 x40y8z1 x40y9z1 x41y10z1 x41y11z1 x41y12z1 x41y13z1 x41y14z1 x41y15z1 x41y16z1 x41y17z1 x41y1z1 x41y2z1 x41y3z1 x41y4z1 x41y5z1 x41y6z1 x41y7z1 x41y8z1 x41y9z1 x42y10z1 x42y11z1 x42y12z1 x42y13z1 x42y14z1 x42y15z1 x42y16z1 x42y17z1 x42y1z1 x42y2z1 x42y3z1 x42y4z1 x42y5z1 x42y6z1 x42y7z1 x42y8z1 x42y9z1 x43y10z1 x43y11z1 x43y12z1 x43y13z1 x43y14z1 x43y15z1 x43y16z1 x43y17z1 x43y1z1 x43y2z1 x43y3z1 x43y4z1 x43y5z1 x43y6z1 x43y7z1 x43y8z1 x43y9z1 x44y10z1 x44y11z1 x44y12z1 x44y13z1 x44y14z1 x44y15z1 x44y16z1 x44y17z1 x44y1z1 x44y2z1 x44y3z1 x44y4z1 x44y5z1 x44y6z1 x44y7z1 x44y8z1 x44y9z1 x45y10z1 x45y11z1 x45y12z1 x45y13z1 x45y14z1 x45y15z1 x45y16z1 x45y17z1 x45y1z1 x45y2z1 x45y3z1 x45y4z1 x45y5z1 x45y6z1 x45y7z1 x45y8z1 x45y9z1 x46y10z1 x46y11z1 x46y12z1 x46y13z1 x46y14z1 x46y15z1 x46y16z1 x46y17z1 x46y1z1 x46y2z1 x46y3z1 x46y4z1 x46y5z1 x46y6z1 x46y7z1 x46y8z1 x46y9z1 x47y10z1 x47y11z1 x47y12z1 x47y13z1 x47y14z1 x47y15z1 x47y16z1 x47y17z1 x47y1z1 x47y2z1 x47y3z1 x47y4z1 x47y5z1 x47y6z1 x47y7z1 x47y8z1 x47y9z1 x4y10z1 x4y11z1 x4y12z1 x4y13z1 x4y14z1 x4y15z1 x4y16z1 x4y17z1 x4y18z1 x4y19z1 x4y3z1 x4y4z1 x4y5z1 x4y6z1 x4y7z1 x4y8z1 x4y9z1 x5y10z1 x5y11z1 x5y12z1 x5y13z1 x5y14z1 x5y15z1 x5y16z1 x5y17z1 x5y18z1 x5y19z1 x5y1z1 x5y2z1 x5y3z1 x5y4z1 x5y5z1 x5y6z1 x5y7z1 x5y8z1 x5y9z1 x6y10z1 x6y11z1 x6y12z1 x6y13z1 x6y14z1 x6y15z1 x6y16z1 x6y17z1 x6y18z1 x6y19z1 x6y1z1 x6y2z1 x6y3z1 x6y4z1 x6y5z1 x6y6z1 x6y7z1 x6y8z1 x6y9z1 x7y10z1 x7y11z1 x7y12z1 x7y13z1 x7y14z1 x7y15z1 x7y16z1 x7y17z1 x7y18z1 x7y19z1 x7y1z1 x7y2z1 x7y3z1 x7y4z1 x7y5z1 x7y6z1 x7y7z1 x7y8z1 x7y9z1 x8y10z1 x8y11z1 x8y12z1 x8y13z1 x8y14z1 x8y15z1 x8y16z1 x8y17z1 x8y18z1 x8y19z1 x8y1z1 x8y2z1 x8y3z1 x8y4z1 x8y5z1 x8y6z1 x8y7z1 x8y8z1 x8y9z1 x9y10z1 x9y11z1 x9y12z1 x9y13z1 x9y14z1 x9y15z1 x9y16z1 x9y17z1 x9y18z1 x9y19z1 x9y1z1 x9y2z1 x9y3z1 x9y4z1 x9y5z1 x9y6z1 x9y7z1 x9y8z1 x9y9z1'

folder_path = '/data/ooicc/pcf-fengshan/completed-Grid/case-files'
#folder_path = '/data/ooicc/pcf-fengshan/completed-Table/case-files'

heights = [80, 100, 125, 150]
#heights = [80, 150]

with open('sample-cases-grid.scm', 'w') as file:

  for filename in sorted(os.listdir(folder_path)):

    file_path = os.path.join(folder_path, filename)

    if "cas.h5" in filename:

      if "Grid" in filename:

        x_str = filename[-12:-10]
        y_str = filename[-9:-7]
        #print(x_str)
        #print(y_str)

        for h in heights:

          output_fn = 'surf-avg-grid-' + x_str + '-' + y_str + '-' + str(h) + '.txt'
          write_lines(h, file_path, output_fn, location_names)

      if "Table-2-base-P" in filename:
        if "large" not in filename:

          xx_str = filename.split('.')[0]
          x_str = xx_str.split('-')[-1]
          #print(x_str)

          for h in heights:

            output_fn = 'surf-avg-table-' + x_str + '-' + str(h) + '.txt'
            write_lines(h, file_path, output_fn, location_names)



