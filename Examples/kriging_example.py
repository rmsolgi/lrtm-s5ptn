
# -*- coding: utf-8 -*-
"""
@author: Ryan Solgi
"""

import lrtm_s5ptn.tropomi.no2 as lrtm
import os
import numpy as np


if __name__=='__main__':
    current_file_path = os.path.abspath(__file__)

    raster_directory=os.path.join(os.path.dirname(current_file_path), 'example_rasters')
    writing_directory=os.path.join(os.path.dirname(current_file_path), 'outputs')
    missing_indices_directory=os.path.join(os.path.dirname(current_file_path), 'indices')
    
    ##########################################################################
    start_date ='20190101'
    end_date='20190201'
    qa_value='0.5'
    resolution='050'
    
    added_missing_ratio=0.03
    string_added_missing_ratio=str(added_missing_ratio)
    
    
    
    indices_file_name='added_missing_indices_'+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'_'+string_added_missing_ratio+'.npy'
    random_indices_path=os.path.join(missing_indices_directory,indices_file_name)
    with open(random_indices_path, 'rb') as random_indices_file:
        random_indices=tuple(np.load(random_indices_file))
        
    
    results=lrtm.imputation.kriging('ordinary',raster_directory,start_date,end_date,resolution,qa_value,random_indices,string_added_missing_ratio,writing_directory,partitioning=False,variogram_model='exponential')
    