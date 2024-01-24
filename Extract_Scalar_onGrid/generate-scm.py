# Script written by Ge Zhengwei
# Institute of High Performance Computing, Singapore
# Copyright (c) 2023. 

import os

filename = 'export-ps-h80cm.scm'
height = 0.8
gap = 0.5

x_min = -11.5
y_min = -4.5
x_max = 12
y_max = 7.5
a = (x_max - x_min) / gap
b = (y_max - y_min) / gap

#print(a)  # Use 'print' to display the value of 'a'


with open(filename, 'w') as file:
    file.write('(define (extract-ps) ;;name of the journal-function\n')
    file.write('        (ti-menu-load-string " /surface/plane-slice z1 0 0 1 ' + str(height) + ' ")\n')
    for i in range(int(b)):  # Cast 'a' to an integer for the range function
        file.write('        (ti-menu-load-string " /surface/iso-clip y-coordinate y' + str(i + 1) + 'z1' + ' z1' + ' ' + str(y_min + gap * i) + ' ' + str(y_min + gap * (i + 1)) + ' ")\n')  # Fixed the string
        for j in range(int(a)):
            file.write('        (ti-menu-load-string " /surface/iso-clip x-coordinate x' + str(j + 1) + 'y' + str(i + 1) + 'z1' + ' y' + str(i + 1) + 'z1' + ' ' + str(x_min + gap * j) + ' ' + str(x_min + gap * (j + 1)) + ' ")\n')


    file.write(' )')
