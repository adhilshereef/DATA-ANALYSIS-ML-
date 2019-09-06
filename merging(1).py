#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import os.path
import shutil


# In[ ]:


path = os.getcwd()
j=0


os.chdir("path\\to\\folder\\")   
os.mkdir("image_with_xml")     
newpath =  "path\\to\\folder\\"+"image_with_xml" 


# In[ ]:


while j < len(glob.glob(path+"\\*"))-1:  
    a=glob.glob(path+"\\*")[j]

    b=glob.glob(path+"\\*")[j+1]


    print(a)
    a1 = os.path.splitext(a)[0]
    b1 = os.path.splitext(b)[0]


# In[ ]:


if a1==b1:
        j=j+2
        shutil.copy(a,newpath)   
        shutil.copy(b,newpath) .
    else:
        j=j+1

