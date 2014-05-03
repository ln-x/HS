from __future__ import division, print_function
from math import pow, sqrt, log, atan, sin, cos, pi, tan, acos, exp,radians, log10
from random import randint
from bisect import bisect

hour = 12
JD = 169
Zenit = 29
Elevation = 300

F_Glo = [0]*8
F_Diffuse = [0]*8
F_Direct = [0]*8

pot = []
ratio_glopot_ref = []
ratio_dirglo = []

# Rad_Vec = 1 + 0.017 * cos((2 * pi / 365) * (186 - JD + hour / 24))
Solar_Constant = 1367 #W/m2

#import reference global radiation at clear sky (pot) TODO: Schoener waere es statt dem Lookup table eine Parametrisierung zu haben...
with open('C:\\heatsource900b5_339\\pot_rows.txt', 'r') as f1:
     data1 = f1.readlines()
f1.closed

for i in data1:
    pot.append(i.split())

print (pot)

zenith_pot = min(enumerate(map(float, pot[0])), key= lambda x: abs(x[1] - Zenit))
print (zenith_pot)

F_Glo[0] = float(pot[1][zenith_pot[0]])

print (F_Glo[0])

F_Glo[1] = 900
F_Diffuse[0] = 0
ratio_glopot_act = F_Glo[1]/F_Glo[0]  ## UHRZEIT
#print ("ratio_glopot_act=", ratio_glopot_act)
#print ("type(ratio_glopot_act)=",type(ratio_glopot_act))

#find to which libRadtran simulated zenith angle is the actual zenith the closest
zenith_ref = [23.85833,28.82833,33.85333,38.8875,43.81917,48.85667,53.82417,
              58.825,63.8125,68.83,73.83333,78.85583,83.83583,88.8375,93.79833]
zenith_act = min(enumerate(zenith_ref), key= lambda x: abs(x[1] - Zenit))
#print ("zenith_act[0]=", zenith_act[0])

with open('C:\\heatsource900b5_339\\ratio_glopot.txt', 'r') as f1:
     data1 = f1.readlines()
f1.closed

for i in data1:
    ratio_glopot_ref.append(i.split())

#print ("ratio_glopot_ref=", ratio_glopot_ref) # ratio glopot ref fuer tau 0,0.1,...1.9,2,3,4,5 bei zenith 23,28,33,38,...bis88deg
#print ("ratio_glopot_ref[0]=", ratio_glopot_ref[0]) # ratio glopot ref fuer tau 0,0.1,...1.9,2,3,4,5 bei zenith[0]23deg
print ("ratio_glopot_ref[zenith_act[0]]=", ratio_glopot_ref[zenith_act[0]])
print ("type(ratio_glopot_ref[zenith_act[0]][0])=", type(ratio_glopot_ref[zenith_act[0]][0]))

with open ('C:\\heatsource900b5_339\\ratio_dirglo.txt', 'r') as f2:
         data2 = f2.readlines()
f2.closed

for i in data2:
    ratio_dirglo.append(i.split())

#print ("ratio_dirglo=", ratio_dirglo)
#print ("ratio_dirglo[0]=", ratio_dirglo[0])


#find to which libRadtran simulated global/potential radiation ratio is the actual measured ratio the closest
ratio_glopot = min(enumerate(map(float,ratio_glopot_ref[zenith_act[0]])), key=lambda x: abs(x[1] - ratio_glopot_act))
#print (ratio_glopot)

#find libRadtran simulated dir/global ratio correspondant to global/pot ratio
ratio_dirglo_act = ratio_dirglo[ratio_glopot[0]][zenith_act[0]]
#print ("type(ratio_dirglo_act)=", type(ratio_dirglo_act))


#Calculate Diffuse Fraction

F_Diffuse[0] = F_Glo[1]*(1 - float(ratio_dirglo_act))
F_Direct[0] = F_Glo[1]* float(ratio_dirglo_act)

print (F_Diffuse[0])
print (F_Direct[0])



