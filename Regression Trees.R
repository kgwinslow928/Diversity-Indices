#Input your values here, highlight, then press "Run"
NHYP1 = 20 #Number of brachydont species (Score = 1)
NHYP2 = 8 #number of mesodont species (Score = 2)
NHYP3 = 3 #Number of hypsodont species (Score = 3)

#Highlight & press "Run"
NHYP = NHYP1+NHYP2+NHYP3 #Number of total species with hypsodonty values

#Define proportions 
#Highlight & press "Run"
pHYP1= NHYP1/NHYP
pHYP2= NHYP2/NHYP
pHYP3= NHYP3/NHYP

#Input your values here
#Highlight & press "Run"
DIETF = 30 #Number of fruit eaters
DIETO = 5 #Number of omnivores
DIETG = 7 #Number of grazers
DIETB = 16 #Number of browsers
DIETM = 12 #number of mixed feeders 
NDIET = DIETF+DIETO+DIETG+DIETB+DIETM  #Number of total species with diet types available for analysis


#Define proportions. 
#Highlight & press "Run"
pDIETF = DIETF/NDIET
pDIETG = DIETG/NDIET
pDIETB = DIETB/NDIET
pDIETM = DIETM/NDIET
pDIETO = DIETO/NDIET

#Mean Annual Precipitation Hypsodonty-only regression tree
#Highlight & press "Run"- Output will be the result of the regression tree. 
if (NHYP1 < 11.5 && pHYP3 >= 0.1938 && pHYP3>=0.4808){
  print("mean annual precipitation = 200.9 mm");x1=200.9
} else if (NHYP1 < 11.5 && pHYP3 >= 0.1938 && pHYP3<0.4808 && pHYP2<0.1277){
  print("mean annual precipitation = 399.7 mm");x1=399.7
} else if (NHYP1 < 11.5 && pHYP3 >= 0.1938 && pHYP3<0.4808 && pHYP2>=0.1277){
  print("mean annual precipitation = 681.6 mm");x1=681.6
} else if (NHYP1 < 11.5 && pHYP3 < 0.1938 && NHYP1 <6.5){
  print("mean annual precipitation = 733.1 mm");x1=733.1
} else if (NHYP1 < 11.5 && pHYP3 < 0.1938 && NHYP1 >=6.5){
  print("mean annual precipitation = 1405 mm");x1=1405
} else if (NHYP1 >= 11.5 && NHYP3 >=3.5 && pHYP3 >= 0.3168){ 
  print("mean annual precipitation = 881.8 mm");x1=881.8
} else if (NHYP1 >= 11.5 && NHYP3 >=3.5 && pHYP3 <0.3168){ 
  print("mean annual precipitation = 1426 mm");x1=1426
} else {
  print("mean annual precipitation = 1939 mm");x1=1939
}

#Mean Annual Precipitation Diet-only regression tree
#Highlight & press "Run"- Output will be the result of the regression tree. 
if (pDIETF < 0.1404 && pDIETM >= 0.2393 && pDIETB<0.2029){
  print("mean annual precipitation = 289.2 mm");x2=289.2
} else if (pDIETF < 0.1404 && pDIETM >= 0.2393 && pDIETB>=0.2029){
  print("mean annual precipitation = 505.3 mm");x2=505.3
} else if (pDIETF < 0.1404 && pDIETM < 0.2393){
  print("mean annual precipitation = 978.2 mm");x2=978.2
} else if (pDIETF >= 0.1404 && pDIETM >= 0.1791 && pDIETM >=0.7321){
  print("mean annual precipitation = 96.35 mm");x2=96.35
} else if (pDIETF >= 0.1404 && pDIETM >= 0.1791 && pDIETM <0.7321){
  print("mean annual precipitation = 1249 mm");x2=1249
} else if (pDIETF >= 0.1404 && pDIETM < 0.1791 && DIETO < 2.5){
  print("mean annual precipitation = 1526 mm");x2=1526
} else if (pDIETF >= 0.1404 && pDIETM < 0.1791 && DIETO >= 2.5 && DIETG >= 1.5){
  print("mean annual precipitation = 1475 mm");x2=1475
} else {
  print("mean annual precipitation = 2253 mm");x2=2253
}

#Mean Annual Precipitation hßypsodonty and diet regression tree
#Highlight & press "Run"- Output will be the result of the regression tree. 
if (pDIETF < 0.1404 && pHYP3 >= 0.4919){
  print("mean annual precipitation = 214.6 mm");x3=214.6
} else if (pDIETF < 0.1404 && pHYP3 < 0.4919 && pDIETM>=0.2393 && pHYP3>=0.1339){
  print("mean annual precipitation = 462.2 mm");x3=462.2
} else if (pDIETF < 0.1404 && pHYP3 < 0.4919 && pDIETM>=0.2393 && pHYP3<0.1339){
  print("mean annual precipitation = 703.9 mm");x3=703.9
} else if (pDIETF < 0.1404 && pHYP3 < 0.4919 && pDIETM<0.2393){
  print("mean annual precipitation = 988.8 mm");x3=988.8
} else if (pDIETF >= 0.1404 && pHYP3 >= 0.2929 && pHYP1 <0.3375){
  print("mean annual precipitation = 145 mm");x3=145
} else if (pDIETF >= 0.1404 && pHYP3 >= 0.2929 && pHYP1 >=0.3375){
  print("mean annual precipitation = 983.5 mm");x3=983.5
} else if (pDIETF >= 0.1404 && pHYP3 < 0.2929 && pDIETF < 0.5417 && pDIETF < 0.2053){
  print("mean annual precipitation = 1346 mm");x3=1346
} else if (pDIETF >= 0.1404 && pHYP3 < 0.2929 && pDIETF < 0.5417 && pDIETF >= 0.2053 && pDIETO < 0.1559){
  print("mean annual precipitation = 1592 mm");x3=1592
} else if (pDIETF >= 0.1404 && pHYP3 < 0.2929 && pDIETF < 0.5417 && pDIETF >= 0.2053 && pDIETO >= 0.1559 && pHYP2<0.04881 && pDIETM >=0.09545){
  print("mean annual precipitation = 1211 mm");x3=1211
} else if (pDIETF >= 0.1404 && pHYP3 < 0.2929 && pDIETF < 0.5417 && pDIETF >= 0.2053 && pDIETO >= 0.1559 && pHYP2<0.04881 && pDIETM <0.09545){
  print("mean annual precipitation = 2074 mm");x3=2074
} else if (pDIETF >= 0.1404 && pHYP3 < 0.2929 && pDIETF < 0.5417 && pDIETF >= 0.2053 && pDIETO >= 0.1559 && pHYP2>=0.04881){
  print("mean annual precipitation = 2578 mm");x3=2578
} else {
  print("mean annual precipitation = 2561 mm");x3=2561
}



#Wettest quarter precipitation hypsodonty only regression tree
#Highlight & press "Run"- Output will be the result of the regression tree. 
if (NHYP1<6.5 && pHYP3>=0.4143){
  print("wettest quarter precipitation = 97.16 mm");y1=97.16
} else if (NHYP1<6.5 && pHYP3<0.4143 && NHYP2<1.5){
  print("wettest quarter precipitation = 222.4 mm");y1=222.4
} else if (NHYP1<6.5 && pHYP3<0.4143 && NHYP2>=1.5 && pHYP1<0.6458 && NHYP2<2.5){
  print("wettest quarter precipitation = 436.7 mm");y1=436.7
} else if (NHYP1<6.5 && pHYP3<0.4143 && NHYP2>=1.5 && pHYP1<0.6458 && NHYP2>=2.5){
  print("wettest quarter precipitation = 882.2 mm");y1=882.2
} else if (NHYP1<6.5 && pHYP3<0.4143 && NHYP2>=1.5 && pHYP1>=0.6458){
  print("wettest quarter precipitation = 1397 mm");y1=1397
} else if (NHYP1>=6.5 && pHYP1<0.5683 && pHYP2>=0.1091 && pHYP3>=0.4015){
  print("wettest quarter precipitation = 274.4 mm");y1=274.4
} else if (NHYP1>=6.5 && pHYP1<0.5683 && pHYP2>=0.1091 && pHYP3<0.4015){
  print("wettest quarter precipitation = 565.9 mm");y1=565.9
} else if (NHYP1>=6.5 && pHYP1<0.5683 && pHYP2<0.1091){
  print("wettest quarter precipitation = 542.6 mm");y1=542.6
} else if (NHYP1>=6.5 && pHYP1>=0.5683 && NHYP<12.5){
  print("wettest quarter precipitation = 587.9 mm");y1=587.9
} else {
  print("wettest quarter precipitation = 799.4 mm");y1=799.4
}



#Wettest quarter precipitation diet type only regression tree
#Highlight & press "Run"- Output will be the result of the regression tree. 
if (pDIETF<0.1404 && DIETF<0.5 && pDIETB<0.1548){
  print("wettest quarter precipitation = 74.46 mm");y2=74.46
} else if (pDIETF<0.1404 && DIETF<0.5 && pDIETB>=0.1548 && DIETM>=1.5){
  print("wettest quarter precipitation = 185.6 mm");y2=185.6
} else if (pDIETF<0.1404 && DIETF<0.5 && pDIETB>=0.1548 && DIETM<1.5){
  print("wettest quarter precipitation = 305.1 mm");y2=305.1
} else if (pDIETF<0.1404 && DIETF>=0.5 && pDIETM>=0.2393){
  print("wettest quarter precipitation = 333.3 mm");y2=333.3
} else if (pDIETF<0.1404 && DIETF>=0.5 && pDIETM<0.2393){
  print("wettest quarter precipitation = 584.3 mm");y2=584.3
} else if (pDIETF>=0.1404 && pDIETO<0.01786){
  print("wettest quarter precipitation = 239.9 mm");y2=239.9
} else if (pDIETF>=0.1404 && pDIETO>=0.01786 && pDIETM>=0.08514 && NDIET<11.5){
  print("wettest quarter precipitation = 527.3 mm");y2=527.3
} else if (pDIETF>=0.1404 && pDIETO>=0.01786 && pDIETM>=0.08514 && NDIET>=11.5 && DIETB>=0.5){
  print("wettest quarter precipitation = 712.5 mm");y2=712.5
} else if (pDIETF>=0.1404 && pDIETO>=0.01786 && pDIETM>=0.08514 && NDIET>=11.5 && DIETB<0.5){
  print("wettest quarter precipitation = 1244 mm");y2=1244
} else {
  print("wettest quarter precipitation = 888.3 mm");y2=888.3
}
  


#Wettest quarter precipitation hypsodonty and diet type regression tree
#Highlight & press "Run" - Output will be the result of the regression tree. 
if (pDIETF<0.1404 && DIETF<0.5 && pHYP3>=0.4143){
  print("wettest quarter precipitation = 88.27 mm");y3=88.27
} else if (pDIETF<0.1404 && DIETF<0.5 && pHYP3<0.4143){
  print("wettest quarter precipitation = 223 mm");y3=223
} else if (pDIETF<0.1404  &&  DIETF>=0.5  &&  pHYP3>=0.4059  &&  DIETG<9.5){
  print("wettest quarter precipitation = 230.8 mm");y3=230.8
} else if (pDIETF<0.1404  &&  DIETF>=0.5  &&  pHYP3>=0.4059  &&  DIETG>=9.5){
  print("wettest quarter precipitation = 564.4 mm");y3=564.4
} else if (pDIETF<0.1404  &&  DIETF>=0.5  &&  pHYP3<0.4059){
  print("wettest quarter precipitation = 551.9 mm");y3=551.9
} else if (pDIETF>=0.1404  &&  pHYP1<0.3167){
  print("wettest quarter precipitation = 75.32 mm");y3=75.32
} else if (pDIETF>=0.1404  &&  pHYP1>=0.3167  &&  pDIETM>=0.08514  &&  pHYP2<0.1571  &&  NHYP<13.5){
  print("wettest quarter precipitation = 452.6 mm");y3=452.6
} else if (pDIETF>=0.1404  &&  pHYP1>=0.3167  &&  pDIETM>=0.08514  &&  pHYP2<0.1571  &&  NHYP>=13.5){
  print("wettest quarter precipitation = 707.4 mm");y3=707.4
} else if (pDIETF>=0.1404  &&  pHYP1>=0.3167  &&  pDIETM>=0.08514  &&  pHYP2>=0.1571){
  print("wettest quarter precipitation = 1022 mm");y3=1022
} else {
  print("wettest quarter precipitation = 882.7 mm");y3=882.7
}




#Driest quarter precipitation hypsodonty only regression tree
#Highlight & press "Run"- Output will be the result of the regression tree. 
if (pHYP3>=0.1181 && pHYP3>=0.3798){
  print("driest quarter precipitation = 14.98 mm");z1=14.98
} else if (pHYP3>=0.1181 && pHYP3<0.3798){
  print("driest quarter precipitation = 50.98 mm");z1=50.98
} else if (pHYP3<0.1181 && NHYP1<14.5){
  print("driest quarter precipitation = 113.8 mm");z1=113.8
} else if (pHYP3<0.1181 && NHYP1>=14.5 && pHYP3<0.04058 && NHYP<21.5 && NHYP1>=20.5){
  print("driest quarter precipitation = 84.25 mm");z1=84.25
} else if (pHYP3<0.1181 && NHYP1>=14.5 && pHYP3<0.04058 && NHYP<21.5 && NHYP1<20.5){
  print("driest quarter precipitation = 206.2 mm");z1=206.2
} else if (pHYP3<0.1181 && NHYP1>=14.5 && pHYP3<0.04058 && NHYP>=21.5 && NHYP>=24.5){
  print("driest quarter precipitation = 175.3 mm");z1=175.3
} else if (pHYP3<0.1181 && NHYP1>=14.5 && pHYP3<0.04058 && NHYP>=21.5 && NHYP<24.5){
  print("driest quarter precipitation = 312.2 mm");z1=312.2
} else if (pHYP3<0.1181 && NHYP1>=14.5 && pHYP3>=0.04058){
  print("driest quarter precipitation = 208.1 mm");z1=208.1
} else {
  print("driest quarter precipitation = 493 mm");z1=493
}




#Driest quarter precipitation diet type only regression tree
#Highlight & press "Run" - Output will be the result of the regression tree. 
if (pDIETF<0.3141 && pDIETB<0.3515 && pDIETG>=0.1952){
  print("driest quarter precipitation = 9.946 mm"); z2=9.946
} else if (pDIETF<0.3141 && pDIETB<0.3515 && pDIETG<0.1952 && DIETO<3.5){
  print("driest quarter precipitation = 43.41 mm"); z2=43.41
} else if (pDIETF<0.3141 && pDIETB<0.3515 && pDIETG<0.1952 && DIETO>=3.5){
  print("driest quarter precipitation = 315.7 mm"); z2=315.7
} else if (pDIETF<0.3141 && pDIETB>=0.3515 && NDIET<16.5 && pDIETB<0.5192){
  print("driest quarter precipitation = 77.08 mm"); z2=77.08
} else if (pDIETF<0.3141 && pDIETB>=0.3515 && NDIET<16.5 && pDIETB>=0.5192){
  print("driest quarter precipitation = 135.3 mm"); z2=135.3
} else if (pDIETF<0.3141 && pDIETB>=0.3515 && NDIET>=16.5 && pDIETO<.1471){
  print("driest quarter precipitation = 117.3 mm"); z2=117.3
} else if (pDIETF<0.3141 && pDIETB>=0.3515 && NDIET>=16.5 && pDIETO>=.1471){
  print("driest quarter precipitation = 544.7 mm"); z2=544.7
} else if (pDIETF>=0.3141 && pDIETF<0.5417 && pDIETG >=0.06275){
  print("driest quarter precipitation = 36.43 mm"); z2=36.43
} else if (pDIETF>=0.3141 && pDIETF<0.5417 && pDIETG<0.06275){
  print("driest quarter precipitation = 173.1 mm"); z2=173.1
} else if (pDIETF>=0.3141 && pDIETF<0.5417 && pDIETO < 0.1603){
  print("driest quarter precipitation = 234.1 mm"); z2=234.1
} else {
  print("driest quarter precipitation = 416.4 mm"); z2=416.4
}



#Driest quarter precipitation hypsodonty and diet type regression tree
#Highlight & press "Run" - Output will be the result of the regression tree. 
if (pHYP3>=0.1181 && pHYP3>=0.3798){
  print("driest quarter precipitation = 14.98 mm"); z3 =14.98
} else if (pHYP3>=0.1181 && pHYP3<0.3798){
  print("driest quarter precipitation = 50.98 mm"); z3 =50.98
} else if (pHYP3<0.1181 && NDIET<16.5 && pDIETF<0.5479 && DIETM>=1.5){
  print("driest quarter precipitation = 92.02 mm"); z3 =92.02
} else if (pHYP3<0.1181 && NDIET<16.5 && pDIETF<0.5479 && DIETM<1.5){
  print("driest quarter precipitation = 133.3 mm"); z3 =133.3
} else if (pHYP3<0.1181 && NDIET<16.5 && pDIETF>=0.5479){
  print("driest quarter precipitation = 376 mm"); z3=376
} else if (pHYP3<0.1181 && NDIET>=16.5 && NHYP>=24.5){
  print("driest quarter precipitation = 172.1 mm"); z3=172.1
} else if (pHYP3<0.1181 && NDIET>=16.5 && NHYP<24.5 && pDIETO<0.1539){
  print("driest quarter precipitation = 207.5 mm"); z3 =207.5
} else {
  print("driest quarter precipitation = 443.5 mm"); z3=443.5
}

#Table with your final results
t1 <- c(x1,x2,x3)
t2 <- c("MAP HYP ONLY","MAP DIET ONLY","MAP HYP+DIET")
results <- table(t1,t2)
results

#Export table to excel 



