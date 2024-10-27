# LRTM-S5PTN

The LRTM-S5PTN was developed to investigate the low rank properties of large scale spatiotemporal atmospheric variables with low rank tensor modeling (LERTM) of Sentinel-5P TROPOMI Tropospheric NO2 (S5PTN). 

The workflow is as follows:
1- Point data should be downloaded from GES DISC.
2- The point data is converted to rasters based on given qa_value, date_interval, and resolutions (see an example code here).
3- Missing indices are prepared as a numpy array (see an example here).
4- The tensor completion and Kriging are run to fill the missing values (see an example here). The output is a dictionary file having metrics and logs.

The current codes is work for CONUS region bounded over the region by the coordinates 20N, 55N, 130W, 60W. Also, the converter generate rasters of resolution 0.05, 0.1, 0.25, 0.5, and 0.1. If a different regions and different resolution are desired the source code must be modified. The naming of the files are based on names at the time data were downloaded from GES DISC. 





