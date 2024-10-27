# -*- coding: utf-8 -*-
"""
@author: Ryan solgi

ATTENTION: One needs to download point data from nasa and set read_directory and writing_directory to make this code functional.
Due to large size of point data, git cannot be used to upload the initial data required for this code.
When data is downloaded for different days, the code iterates over each day and generate daily rasters.
"""
read_directory="Set a directory where point data are available"
write_directory="Set a directory where output rasters are saved"


from datetime import datetime
from datetime import timedelta
from lrtm_s5ptn.tropomi.no2.converter import converter_run
import os

def generate_date_list(start_date,end_date):  
    
    date=datetime.strptime(start_date,'%Y%m%d')
    stop_date=datetime.strptime(end_date,'%Y%m%d')
    granule_end_date_list=[]

    while date<=stop_date:
        granule_end_date=date.date().strftime('%Y%m%d')
        granule_end_date_list.append(granule_end_date)
        
        date+=timedelta(days=1)
    return granule_end_date_list




current_file_path = os.path.abspath(__file__)
raster_directory=os.path.join(os.path.dirname(current_file_path), 'raster_templates')


start_date ='20230616' #change start date, format: YYYYMMDD
end_date='20230616' #change end date 


granule_end_date_list=generate_date_list(start_date,end_date)


for d in granule_end_date_list:
    converter_run(read_directory, write_directory,raster_directory, d, 0.5)
    
    

     
