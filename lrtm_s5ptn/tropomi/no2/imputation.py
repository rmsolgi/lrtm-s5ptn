# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:08:56 2023

@author: Ryan
"""


import numpy as np
import os
import lrtm_s5ptn.tropomi.no2 as hp
import time
import pickle
import tensorlearn as tl

def low_rank_inquiry(rank_list,cp_iteration, raster_directory,start_date,end_date,resolution,qa_value, writing_directory=None, verbose=True):
    data, existed_dates, missed_dates=hp.utils.raster_to_array(raster_directory,start_date,end_date,resolution,qa_value)
    data=hp.utils.add_nans(data) #### nan values must be added before any change in the data values 
    data=hp.utils.molec_per_cm2(data)
    data_array=(data-np.nanmin(data))/(np.nanmax(data)-np.nanmin(data))
    mask=hp.utils.make_mask(data)
    data_array[np.where(np.isnan(data_array))]=0
    projected_tensor=np.multiply(data_array,mask)
    
    norm_error_list=[]
    data_norm=tl.tensor_frobenius_norm(data_array)
    for rank in rank_list:
        weights,factors=tl.cp_als_rand_init(projected_tensor, rank, cp_iteration)

        tensor_hat=tl.cp_to_tensor(weights,factors)

        error=tensor_hat-data_array

        norm_error=tl.tensor_frobenius_norm(error)
        norm_error_list.append(norm_error/data_norm)
        if verbose: 
            print('finished rank: ', rank)

    results_dict={}
    results_dict['ranks']=rank_list
    results_dict['errors']=norm_error_list
    if writing_directory!=None:
        file_name="low_rank_inquiry"+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'.pickle'
        writing_file=os.path.join(writing_directory, file_name)
        with open(writing_file, 'wb') as file:
            pickle.dump(results_dict,file)
    return results_dict


def tensor_completion(rank,iteration,raster_directory,start_date,end_date,resolution,qa_value,random_indices, added_missing_ratio, writing_directory=None):
    #random_indices_name="random_indices_"+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'_'+added_missing_ratio+'.npy'
    data, existed_dates, missed_dates=hp.utils.raster_to_array(raster_directory,start_date,end_date,resolution,qa_value)
    data=hp.utils.add_nans(data) #### nan values must be added before any change in the data values 
    data=hp.utils.molec_per_cm2(data)
    mask=hp.utils.make_mask(data)
    #random_indices=hp.utils.read_added_missing_indices(random_indices_name)
    mask[random_indices]=0
    raw_observations=data[random_indices]
    data_array=(data-np.nanmin(data))/(np.nanmax(data)-np.nanmin(data))
    normalized_observations=data_array[random_indices]
    start=time.time()
    reterived_array, error_log=hp.cp_completion.run_cp_completion(data_array, mask, rank, iteration)
    end=time.time()
    normalized_predictions=reterived_array[random_indices]
    raw_reterived_array=reterived_array*(np.nanmax(data)-np.nanmin(data))+np.nanmin(data)
    raw_predictions=raw_reterived_array[random_indices]
    
    results_dict={}
    results_dict['log']=error_log
    results_dict['run_time']=end-start
    results_dict['normalized_observations']=normalized_observations
    results_dict['normalized_predictions']=normalized_predictions
    results_dict['raw_observations']=raw_observations
    results_dict['raw_predictions']=raw_predictions
    results_dict['indices']=random_indices
    if writing_directory!=None:
        file_name="TC_results_"+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'_'+added_missing_ratio+'_'+str(rank)+'.pickle'
        writing_file=os.path.join(writing_directory, file_name)
        with open(writing_file, 'wb') as file:
            pickle.dump(results_dict,file)
        
    return results_dict

def kriging(kriging_type,raster_directory,start_date,end_date,resolution,qa_value,random_indices,added_missing_ratio, writing_directory=None, partitioning=False, variogram_model='linear'):
    
    #random_indices_name="random_indices_"+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'_'+added_missing_ratio+'.npy'
    data, existed_dates, missed_dates=hp.utils.raster_to_array(raster_directory,start_date,end_date,resolution,qa_value)
    data=hp.utils.add_nans(data) #### nan values must be added before any change in the data values 
    data=hp.utils.molec_per_cm2(data)
    #mask=hp.utils.make_mask(data)  IT MUST NOT USE BECAUSE IT INCLUDE NAN VALUES TOO. 
    mask=np.ones(data.shape)
    #random_indices=hp.utils.read_added_missing_indices(random_indices_name)
    mask[random_indices]=0
    
    #cut data
    #cut_mask=mask[prediction_interval[0]:prediction_interval[1],:,:]

    #cut_random_indices=np.where(cut_mask==0)
    #cut_data=data[prediction_interval[0]:prediction_interval[1],:,:]
    
    
    
    raw_observations=data[random_indices]
    data_array=(data-np.nanmin(data))/(np.nanmax(data)-np.nanmin(data))
    #cut_data_array=data_array[prediction_interval[0]:prediction_interval[1],:,:]
    normalized_observations=data_array[random_indices]
    start=time.time()
    
    reterived_array=hp.kriging.run_kriging(data_array,mask,resolution, kriging_type,variogram_model, partitioning)
    
    end=time.time()
    
    normalized_predictions=reterived_array[random_indices]
    raw_reterived_array=reterived_array*(np.nanmax(data)-np.nanmin(data))+np.nanmin(data)
    raw_predictions=raw_reterived_array[random_indices]
    
    results_dict={}
    results_dict['run_time']=end-start
    results_dict['normalized_observations']=normalized_observations
    results_dict['normalized_predictions']=normalized_predictions
    results_dict['raw_observations']=raw_observations
    results_dict['raw_predictions']=raw_predictions
    results_dict['indices']=random_indices
    if writing_directory!=None:
        file_name=kriging_type+"_K_results_"+start_date+'_'+end_date+'_'+resolution+'_'+qa_value+'_'+added_missing_ratio+'_'+'.pickle'
        writing_file=os.path.join(writing_directory, file_name)
        with open(writing_file, 'wb') as file:
            pickle.dump(results_dict,file)
            
    return results_dict
