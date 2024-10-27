# LRTM-S5PTN

The LRTM-S5PTN was developed to investigate the low-rank properties of large-scale spatiotemporal atmospheric variables using low-rank tensor modeling (LRTM) of Sentinel-5P TROPOMI Tropospheric NO₂ (S5PTN).

The workflow is as follows:

Point data need to be downloaded from NASA GES DISC.

Conversion to rasters: The point data from GES DISC is converted to rasters based on specified qa_value, date_interval, and resolutions (see converter_example.py under examples). The source codes for conversion are included here but to run the example code for this step, one first needs to download the data and set directories as commented in the code. The size of the input daily point data exceeds Git's maximum file size. Therefore it was not possible to upload an input file. 


Tensor completion and Kriging: Tensor completion and Kriging are run to fill in the missing values (see lrtm_example.py and kriging_example.py under examples). The output is a dictionary file containing metrics and logs. The example codes on this Git are functional using the example rasters. If additional dates and resolutions are needed, the corresponding rasters should be prepared as described above. Missing indices are prepared as a numpy array (see example_missing_indices under examples).


The current code is configured for the CONUS region, bounded by the coordinates 20°N to 55°N and 130°W to 60°W. Additionally, the converter generates rasters at resolutions of 0.05, 0.1, 0.25, 0.5, and 1.0. If different regions or resolutions are desired, the source code must be modified. File naming is based on the original names when the data were downloaded from GES DISC.


Install the package before runing the examples.

```python
pip install lrtm-s5ptn
```

