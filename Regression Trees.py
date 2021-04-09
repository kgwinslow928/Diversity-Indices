#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Precipitation Python Code using Eronen et al. (2010a) Regression Trees
#Data Needed: Counts of the amount of species for each hypsodont value (1,2,3) & each diet types (F,O,M,G,B)


# In[81]:


#Input your values here then press "Run"
NHYP1 = 4 #Number of brachydont species (Score = 1)
NHYP2 = 7 #number of mesodont species (Score = 2)
NHYP3 = 13 #Number of hypsodont species (Score = 3)


# In[82]:


#Press "Run"
NHYP = NHYP1+NHYP2+NHYP3 #Number of total species with hypsodonty values


# In[83]:


#Define proportions. Simply press "Run"
pHYP1= NHYP1/NHYP
pHYP2= NHYP2/NHYP
pHYP3= NHYP3/NHYP


# In[85]:


#Input your values here then press "Run"
DIETF = 0 #Number of fruit eaters
DIETO = 1 #Number of omnivores
DIETG = 16 #Number of grazers
DIETB = 3 #Number of browsers
DIETM = 5 #number of mixed feeders 


# In[86]:


#Press "Run"
NDIET = DIETF+DIETO+DIETG+DIETB +DIETM  #Number of total species with diet types available for analysis


# In[87]:


#Define proportions. Simply press "Run"
pDIETF = DIETF/NDIET
pDIETG = DIETG/NDIET
pDIETB = DIETB/NDIET
pDIETM = DIETM/NDIET
pDIETO = DIETO/NDIET


# In[88]:


#Mean Annual Precipitation hypsodonty-only regression tree
#Press "Run" - Output will be the result of the regression tree. 
if NHYP1 < 11.5 and pHYP3 >= 0.1938 and pHYP3>=0.4808:
    print("mean annual precipitation = 200.9 mm")
elif NHYP1 < 11.5 and pHYP3 >= 0.1938 and pHYP3<0.4808 and pHYP2<0.1277:
    print("mean annual precipitation = 399.7 mm")
elif NHYP1 < 11.5 and pHYP3 >= 0.1938 and pHYP3<0.4808 and pHYP2>=0.1277:
    print("mean annual precipitation = 681.6 mm")
elif NHYP1 < 11.5 and pHYP3 < 0.1938 and NHYP1 <6.5:
    print("mean annual precipitation = 733.1 mm")
elif NHYP1 < 11.5 and pHYP3 < 0.1938 and NHYP1 >=6.5:
    print("mean annual precipitation = 1405 mm")
elif NHYP1 >= 11.5 and NHYP3 >=3.5 and pHYP3 >= 0.3168: 
    print("mean annual precipitation = 881.8 mm")
elif NHYP1 >= 11.5 and NHYP3 >=3.5 and pHYP3 <0.3168: 
    print("mean annual precipitation = 1426 mm mm")
else:
    print("mean annual precipitation = 1939 mm")


# In[89]:


#Mean Annual Precipitation diet-only regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pDIETF < 0.1404 and pDIETM >= 0.2393 and pDIETB<0.2029:
    print("mean annual precipitation = 289.2 mm")
elif pDIETF < 0.1404 and pDIETM >= 0.2393 and pDIETB>=0.2029:
    print("mean annual precipitation = 505.3 mm")
elif pDIETF < 0.1404 and pDIETM < 0.2393:
    print("mean annual precipitation = 978.2 mm")
elif pDIETF >= 0.1404 and pDIETM >= 0.1791 and pDIETM >=0.7321:
    print("mean annual precipitation = 96.35 mm")
elif pDIETF >= 0.1404 and pDIETM >= 0.1791 and pDIETM <0.7321:
    print("mean annual precipitation = 1249 mm")
elif pDIETF >= 0.1404 and pDIETM < 0.1791 and DIETO < 2.5:
    print("mean annual precipitation = 1526 mm")
elif pDIETF >= 0.1404 and pDIETM < 0.1791 and DIETO >= 2.5 and DIETG >= 1.5:
    print("mean annual precipitation = 1475 mm")
else:
    print("mean annual precipitation = 2253 mm")


# In[90]:


#Mean Annual Precipitation hypsodonty and diet regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pDIETF < 0.1404 and pHYP3 >= 0.4919:
    print("mean annual precipitation = 214.6 mm")
elif pDIETF < 0.1404 and pHYP3 < 0.4919 and pDIETM>=0.2393 and pHYP3>=0.1339:
    print("mean annual precipitation = 462.2 mm")
elif pDIETF < 0.1404 and pHYP3 < 0.4919 and pDIETM>=0.2393 and pHYP3<0.1339:
    print("mean annual precipitation = 703.9 mm")
elif pDIETF < 0.1404 and pHYP3 < 0.4919 and pDIETM<0.2393:
    print("mean annual precipitation = 988.8 mm")
elif pDIETF >= 0.1404 and pHYP3 >= 0.2929 and pHYP1 <0.3375:
    print("mean annual precipitation = 145 mm")
elif pDIETF >= 0.1404 and pHYP3 >= 0.2929 and pHYP1 >=0.3375:
    print("mean annual precipitation = 983.5 mm")
elif pDIETF >= 0.1404 and pHYP3 < 0.2929 and pDIETF < 0.5417 and pDIETF < 0.2053:
    print("mean annual precipitation = 1346 mm")
elif pDIETF >= 0.1404 and pHYP3 < 0.2929 and pDIETF < 0.5417 and pDIETF >= 0.2053 and pDIETO < 0.1559:
    print("mean annual precipitation = 1592 mm")
elif pDIETF >= 0.1404 and pHYP3 < 0.2929 and pDIETF < 0.5417 and pDIETF >= 0.2053 and pDIETO >= 0.1559 and pHYP2<0.04881 and pDIETM >=0.09545:
    print("mean annual precipitation = 1211 mm")
elif pDIETF >= 0.1404 and pHYP3 < 0.2929 and pDIETF < 0.5417 and pDIETF >= 0.2053 and pDIETO >= 0.1559 and pHYP2<0.04881 and pDIETM <0.09545:
    print("mean annual precipitation = 2074 mm")
elif pDIETF >= 0.1404 and pHYP3 < 0.2929 and pDIETF < 0.5417 and pDIETF >= 0.2053 and pDIETO >= 0.1559 and pHYP2>=0.04881:
    print("mean annual precipitation = 2578 mm")
else:
    print("mean annual precipitation = 2561 mm")


# In[116]:


#Wettest quarter precipitation hypsodonty only regression tree
#Press "Run" - Output will be the result of the regression tree. 
if NHYP1<6.5 and pHYP3>=0.4143:
    print("wettest quarter precipitation = 97.16 mm")
elif NHYP1<6.5 and pHYP3<0.4143 and NHYP2<1.5:
    print("wettest quarter precipitation = 222.4 mm")
elif NHYP1<6.5 and pHYP3<0.4143 and NHYP2>=1.5 and pHYP1<0.6458 and NHYP2<2.5:
    print("wettest quarter precipitation = 436.7 mm")
elif NHYP1<6.5 and pHYP3<0.4143 and NHYP2>=1.5 and pHYP1<0.6458 and NHYP2>=2.5:
    print("wettest quarter precipitation = 882.2 mm")
elif NHYP1<6.5 and pHYP3<0.4143 and NHYP2>=1.5 and pHYP1>=0.6458:
    print("wettest quarter precipitation = 1397 mm")
elif NHYP1>=6.5 and pHYP1<0.5683 and pHYP2>=0.1091 and pHYP3>=0.4015:
    print("wettest quarter precipitation = 274.4 mm")
elif NHYP1>=6.5 and pHYP1<0.5683 and pHYP2>=0.1091 and pHYP3<0.4015:
    print("wettest quarter precipitation = 565.9 mm")
elif NHYP1>=6.5 and pHYP1<0.5683 and pHYP2<0.1091:
    print("wettest quarter precipitation = 542.6 mm")
elif NHYP1>=6.5 and pHYP1>=0.5683 and NHYP<12.5:
    print("wettest quarter precipitation = 587.9 mm")
else:
    print("wettest quarter precipitation = 799.4 mm")


# In[117]:


#Wettest quarter precipitation diet type only regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pDIETF<0.1404 and DIETF<0.5 and pDIETB<0.1548:
    print("wettest quarter precipitation = 74.46 mm")
elif pDIETF<0.1404 and DIETF<0.5 and pDIETB>=0.1548 and DIETM>=1.5:
    print("wettest quarter precipitation = 185.6 mm")
elif pDIETF<0.1404 and DIETF<0.5 and pDIETB>=0.1548 and DIETM<1.5:
    print("wettest quarter precipitation = 305.1 mm")
elif pDIETF<0.1404 and DIETF>=0.5 and pDIETM>=0.2393:
    print("wettest quarter precipitation = 333.3 mm")
elif pDIETF<0.1404 and DIETF>=0.5 and pDIETM<0.2393:
    print("wettest quarter precipitation = 584.3 mm")
elif pDIETF>=0.1404 and pDIETO<0.01786:
    print("wettest quarter precipitation = 239.9 mm")
elif pDIETF>=0.1404 and pDIETO>=0.01786 and pDIETM>=0.08514 and NDIET<11.5:
    print("wettest quarter precipitation = 527.3 mm")
elif pDIETF>=0.1404 and pDIETO>=0.01786 and pDIETM>=0.08514 and NDIET>=11.5 and DIETB>=0.5:
    print("wettest quarter precipitation = 712.5 mm")
elif pDIETF>=0.1404 and pDIETO>=0.01786 and pDIETM>=0.08514 and NDIET>=11.5 and DIETB<0.5:
    print("wettest quarter precipitation = 1244 mm")
else:
    print("wettest quarter precipitation = 888.3 mm")


# In[118]:


#Wettest quarter precipitation hypsodonty and diet type regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pDIETF<0.1404 and DIETF<0.5 and pHYP3>=0.4143:
    print("wettest quarter precipitation = 88.27 mm")
elif pDIETF<0.1404 and DIETF<0.5 and pHYP3<0.4143:
    print("wettest quarter precipitation = 223 mm")
elif pDIETF<0.1404 and DIETF>=0.5 and pHYP3>=0.4059 and DIETG<9.5:
    print("wettest quarter precipitation = 230.8 mm")
elif pDIETF<0.1404 and DIETF>=0.5 and pHYP3>=0.4059 and DIETG>=9.5:
    print("wettest quarter precipitation = 564.4 mm")
elif pDIETF<0.1404 and DIETF>=0.5 and pHYP3<0.4059:
    print("wettest quarter precipitation = 551.9 mm")
elif pDIETF>=0.1404 and pHYP1<0.3167:
    print("wettest quarter precipitation = 75.32 mm")
elif pDIETF>=0.1404 and pHYP1>=0.3167 and pDIETM>=0.08514 and pHYP2<0.1571 and NHYP<13.5:
    print("wettest quarter precipitation = 452.6 mm")
elif pDIETF>=0.1404 and pHYP1>=0.3167 and pDIETM>=0.08514 and pHYP2<0.1571 and NHYP>=13.5:
    print("wettest quarter precipitation = 707.4 mm")
elif pDIETF>=0.1404 and pHYP1>=0.3167 and pDIETM>=0.08514 and pHYP2>=0.1571:
    print("wettest quarter precipitation = 1022 mm")
else:
    print("wettest quarter precipitation = 882.7 mm")


# In[119]:


#Driest quarter precipitation hypsodonty only regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pHYP3>=0.1181 and pHYP3>=0.3798:
    print("driest quarter precipitation = 14.98 mm")
elif pHYP3>=0.1181 and pHYP3<0.3798:
    print("driest quarter precipitation = 50.98 mm")
elif pHYP3<0.1181 and NHYP1<14.5:
    print("driest quarter precipitation = 113.8 mm")
elif pHYP3<0.1181 and NHYP1>=14.5 and pHYP3<0.04058 and NHYP<21.5 and NHYP1>=20.5:
    print("driest quarter precipitation = 84.25 mm")
elif pHYP3<0.1181 and NHYP1>=14.5 and pHYP3<0.04058 and NHYP<21.5 and NHYP1<20.5:
    print("driest quarter precipitation = 206.2 mm")
elif pHYP3<0.1181 and NHYP1>=14.5 and pHYP3<0.04058 and NHYP>=21.5 and NHYP>=24.5:
    print("driest quarter precipitation = 175.3 mm")
elif pHYP3<0.1181 and NHYP1>=14.5 and pHYP3<0.04058 and NHYP>=21.5 and NHYP<24.5:
    print("driest quarter precipitation = 312.2 mm")
elif pHYP3<0.1181 and NHYP1>=14.5 and pHYP3>=0.04058:
    print("driest quarter precipitation = 208.1 mm")
else:
    print("driest quarter precipitation = 493 mm")


# In[120]:


#Driest quarter precipitation diet type only regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pDIETF<0.3141 and pDIETB<0.3515 and pDIETG>=0.1952:
    print("driest quarter precipitation = 9.946 mm")
elif pDIETF<0.3141 and pDIETB<0.3515 and pDIETG<0.1952 and DIETO<3.5:
    print("driest quarter precipitation = 43.41 mm")
elif pDIETF<0.3141 and pDIETB<0.3515 and pDIETG<0.1952 and DIETO>=3.5:
    print("driest quarter precipitation = 315.7 mm")
elif pDIETF<0.3141 and pDIETB>=0.3515 and NDIET<16.5 and pDIETB<0.5192:
    print("driest quarter precipitation = 77.08 mm")
elif pDIETF<0.3141 and pDIETB>=0.3515 and NDIET<16.5 and pDIETB>=0.5192:
    print("driest quarter precipitation = 135.3 mm")
elif pDIETF<0.3141 and pDIETB>=0.3515 and NDIET>=16.5 and pDIETO<.1471:
    print("driest quarter precipitation = 117.3 mm")
elif pDIETF<0.3141 and pDIETB>=0.3515 and NDIET>=16.5 and pDIETO>=.1471:
    print("driest quarter precipitation = 544.7 mm")
elif pDIETF>=0.3141 and pDIETF<0.5417 and pDIETG >=0.06275:
    print("driest quarter precipitation = 36.43 mm")
elif pDIETF>=0.3141 and pDIETF<0.5417 and pDIETG<0.06275:
    print("driest quarter precipitation = 173.1 mm")
elif pDIETF>=0.3141 and pDIETF<0.5417 and pDIETO < 0.1603:
    print("driest quarter precipitation = 234.1 mm")
else:
    print("driest quarter precipitation = 416.4 mm")


# In[121]:


#Driest quarter precipitation hypsodonty and diet type regression tree
#Press "Run" - Output will be the result of the regression tree. 
if pHYP3>=0.1181 and pHYP3>=0.3798:
    print("driest quarter precipitation = 14.98 mm")
elif pHYP3>=0.1181 and pHYP3<0.3798:
    print("driest quarter precipitation = 50.98 mm")
elif pHYP3<0.1181 and NDIET<16.5 and pDIETF<0.5479 and DIETM>=1.5:
    print("driest quarter precipitation = 92.02 mm")
elif pHYP3<0.1181 and NDIET<16.5 and pDIETF<0.5479 and DIETM<1.5:
    print("driest quarter precipitation = 133.3 mm")
elif pHYP3<0.1181 and NDIET<16.5 and pDIETF>=0.5479:
    print("driest quarter precipitation = 376 mm")
elif pHYP3<0.1181 and NDIET>=16.5 and NHYP>=24.5:
    print("driest quarter precipitation = 172.1 mm")
elif pHYP3<0.1181 and NDIET>=16.5 and NHYP<24.5 and pDIETO<0.1539:
    print("driest quarter precipitation = 207.5 mm")
else:
    print("driest quarter precipitation = 443.5 mm")


# In[ ]:




