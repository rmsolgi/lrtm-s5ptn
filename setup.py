'''
    Copyright 2023 Ryan Solgi
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of 
    this software and associated documentation files (the "Software"), to deal in 
    the Software without restriction, including without limitation the rights to use, 
    copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
    Software, and to permit persons to whom the Software is furnished to do so, 
    subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
    SOFTWARE.

'''

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lrtm-s5ptn",
    version="1.41",
    author="Ryan Solgi",
    author_email="ryan.solgi@gmail.com",
    maintainer='Ryan Solgi',
    description="Low Rank Tensor Modeling of Sentinel 5P Tropospheric NO2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/rmsolgi/harpia.git",
    keywords=['lrtm-s5ptn'],
    packages=setuptools.find_packages(include=['*'], exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['numpy', 'datetime', 'netCDF4', 'pandas', 'geopandas', 'rasterio', 'tensorlearn'],
    #include_package_data=True,
    #package_data={"harpia": ["tropomi/no2/lib/raster_templates/*.tif"]}
    )







