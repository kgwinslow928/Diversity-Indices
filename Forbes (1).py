#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Input your own data where necessary and press "Run" when instructed 


# In[ ]:


#Defining your variables for Forbes index 
#Input your numbers as instructed and delete the quotation marks
#Press "Run"
a="input number of shared species"
b="input number of unique species at site 1"
c="input number of unique species at site 2"


# In[23]:


#Press"Run"
#This defines your N variable 
N=a+b+c


# In[ ]:


#Press "Run"
#This line of code is simply to check your value of N
N


# In[ ]:


#Press "Run"
#This is the first part of the equation
f1 = N+(math.sqrt(N))


# In[ ]:


#Press "Run"
#This is to check your f1 variable and confirm it is defined
f1


# In[27]:


#Press "Run"
#This is to define f2 (The top of the equation & the first part of the bottom of the equation)
f2 = f*a


# In[ ]:


#Press "Run"
#This is to check your f2 variable and confirm it is defined
f2


# In[29]:


#Press "Run"
#This is the final equation and will compute the Forbes coefficient for you. 
F= f2/(f2+(1.5*b*c))


# In[ ]:


#Press "Run"
#The output of this is your Forbes coefficient 
F


# In[ ]:


#THE NEXT SECTION IS YOUR JACCARD INDEX 


# In[ ]:


#This is the variables input for the Jaccard index
#Place your own data, delete quotation marks, and Press "Run"
j="input number of shared species"
d="input total number of species at site 1"
e="input total number of species at site 2"


# In[ ]:


#This defines your equation and inputs your data for the Jaccard Index 
#Press "Run"
J = (j)/(d+e+j)


# In[ ]:


#Press "Run"
#The output is your Jaccard coefficient 
J

