## Workflow and Scripts to Batch Run Passive Scalar Simulation with Ansys Fluent

Ansys Fluent can be used to simulate the release of a passive scalar source (steady-state) over many different possible locations in a particular domain. 

We frequently need to generate a database of the passive scalar concentration for different release locations, such as in the training of surrogate models for application in other areas.

This is a repo of scripts that help with the above process.

____

The workflow can be described as follows:

1) [Geometry creation with explicit release boxes duplicated across a grid for easy specification as a passive scalar source](./DuplicateReleaseBoxes/Readme.md) 
2) Ansys Fluent Meshing and Solution with standard workflows for the steady-state flow velocity
3) Conversion of case file to handle passive scalar release, with accompanying settings.
4) [Selection of random release locations and solution with Ansys Fluent User-Defined Scalar functionality](./Select_RandLoc_Create_scm_for_Fluent/Readme.md) 
5) [Extraction and output of Passive Scalar concentration throughout domain on pre-defined grid points](./Extract_Scalar_onGrid/Readme.md)
6) Script to extract and compile all the outputs from different Passive Scalar Runs

Scripts and instructions for the various steps are provided in the accompanying subsections.

***
Note 1: This is not an official IHPC product, but please credit this work if this is helpful to you.

Note 2: The Ansys Fluent schema files were created based on Ansys Fluent 2021 version. They have not been tested on other (both older or newer) versions of Ansys Fluent where additional functionalities/options have been added.

Note 3: Python scripts are written for Python version 3.8

This is the work of [Ooi Chin Chun](mailto:ooicc@cfar.a-star.edu.sg) and [Ge Zhengwei](mailto:gezw@ihpc.a-star.edu.sg) from the Institute of High Performance Computing, A*STAR, Singapore.
