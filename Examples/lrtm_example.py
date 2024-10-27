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
    missing_indices_directory=os.path.join(os.path.dirname(current_file_path), 'example_missing_indices')
    
    ###########################################################################
    
    start_date ='20190101'
    end_date='20190201'
    qa_value='0.5'
    resolution='050'
    
    added_missing_ratio=0.03
    string_added_missing_ratio=str(added_missing_ratio)
    ranks=[50] #change rank here
    
    
    indices_file_name='added_missing_indices_'+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'_'+string_added_missing_ratio+'.npy'
    indices_path=os.path.join(missing_indices_directory,indices_file_name)
    with open(indices_path, 'rb') as indices_file:
        random_indices=tuple(np.load(indices_file))
        
    for rank in ranks:
    
        results=lrtm.imputation.tensor_completion(rank,1,raster_directory,start_date,end_date,resolution,qa_value,random_indices,string_added_missing_ratio,writing_directory)

        
    