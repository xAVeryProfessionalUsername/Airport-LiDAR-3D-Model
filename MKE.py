#!/usr/bin/env python
# coding: utf-8

# In[30]:


import arcpy
import os
import pandas as pd
import numpy as np
import shutil


# In[31]:


directory = r"C:\Users\nicks\OneDrive\Desktop\VSprojects\MilwaukeeAirport\lidarmaps"

# List all files in the directory
files = os.listdir(directory)

# Loop through the files and rename them
for index, filename in enumerate(files):
    # Construct the old file path
    old_file = os.path.join(directory, filename)
    
    # Create the new filename with an index
    new_filename = str(index + 1) + '.zip'
    
    # Construct the new file path
    new_file = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file, new_file)


# In[32]:


import os
import zipfile

# Specify the directory containing the ZIP files
directory = r"C:\Users\nicks\OneDrive\Desktop\VSprojects\MilwaukeeAirport\lidarmaps"

# List all files in the directory
files = os.listdir(directory)

# Loop through the files and extract the ZIP files
for filename in files:
    if filename.endswith('.zip'):
        # Construct the full file path
        zip_path = os.path.join(directory, filename)
        
        # Create a directory for the extracted contents
        extract_dir = os.path.join(directory, os.path.splitext(filename)[0])
        os.makedirs(extract_dir, exist_ok=True)
        
        # Extract the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

print("ZIP files have been extracted.")


# In[ ]:





# In[33]:


directory = r"C:\Users\nicks\OneDrive\Desktop\VSprojects\MilwaukeeAirport\lidarmaps"

# List all files in the directory
files = os.listdir(directory)

n = 1
for num, filenum in enumerate(files):
    filefolder = os.path.join(directory, filenum)
    viewfilefolder = os.listdir(filefolder)
    for file in viewfilefolder:
        junkdegree = os.path.join(filefolder, file)
        print(junkdegree)
        newfile =  r"C:\Users\nicks\OneDrive\Desktop\VSprojects\MilwaukeeAirport\lasfiles" + '\\' + str(n) + '.las'
        n+=1
        print(newfile)
        junkdegreedir = os.listdir(junkdegree)
        for plslas in junkdegreedir:
            if '.las' in plslas:
                print(plslas)
                movefile = os.path.join(junkdegree,str(plslas))
                shutil.move(movefile, newfile)

