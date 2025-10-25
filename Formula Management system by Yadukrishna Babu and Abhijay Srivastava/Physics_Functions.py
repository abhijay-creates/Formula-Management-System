import math
import pandas as pd


#transmission of heat(heat transfer chapter)
###############################################
###############################################

def emmisivepower():
    absorbed = float(input("enter the energy absorbed by the body"))
    givenout = float(input("enter the energy given out by the body"))

    em = absorbed/givenout
    return em

def temp_gradient():
    delta0 = int(input("enter the change in temperature of body:"))
    p_dist = int(input("enter the perpendicular distance between the two isothermal surfaces:"))
    temp = delta0/p_dist
    return temp

def thermal_res():
    temp1 = int(input("enter the initial temperature of the body:"))
    temp2 = int(input("enter the final temperature of the body:"))
    temp_dif = temp2-temp1
    h = int(input("enter the rate of flow of heat"))
    res = temp_dif/h
    return res

def equivalent_res_parll():
    r1 = int(input("enter the resistance for the first body"))
    r2 = int(input("enter the resistance for the second body:"))
    r = (r1*r2)/(r1+r2)
    return r


def heatchange():
    HeatType = ""
    temp1 = float(input("enter initial temperature :- "))
    temp2 = float(input("enter final temperature :- "))
    deltatemp = temp2 - temp1
    thermalcoeff = float(input("enter the thermal coefficient :- "))
    area = float(input("enter the crossectional area :- "))
    length = float(input("enter the length :- "))
    heat = (deltatemp*thermalcoeff*area)/length
    return heat



##############################
##############################
#electrostats chapter

def quantization():
    n = int(input("Enter the number of electrons present:"))
    e100 = 1.6*(10^(-19))
    bigq = n*e100
    return bigq


def relative_permeability():
    e0 = 8.854*(10^(-12))
    ee = float(input("enter the relative permeability of the material"))
    e_ = e0/ee
    return e_


def coulomb_law():
    q1 = float(input("enter first body's charge:"))
    q2 = float(input("enter second body's charge:"))
    r300 = float(input("enter the distance between the objects:"))
    k = 9*(10**9)
    force = (k*(q1*q2))/(r300**2)
    return force
    
def electric_field():
    k1 = 9*pow(10,-9)
    r11 = float(input("enter the distance:"))
    q22 = float(input("enter the amount of charge of body:"))
    e = (k1*q22)/pow(r11,2)
    return e

def electric_flux():
    print("This equation works only when the electric field intensity is uniform")
    k2 = 9*pow(10,-9)
    r1 = float(input("enter the distance:"))
    q2 = float(input("enter the amount of charge of body:"))
    e16 = (k2*q2)/pow(r1,2)
    area = float(input("enter the area of the body"))
    theta = float(input("enter the degree of inclination of this body (in degrees):"))
    cos = math.cos(theta)
    flux = (e16*area)*cos
    return flux

####################################
####################################
# mechanics chapter

def motion1():
    u1 = int(input("initial velocity:"))
    a1 = int(input("acceleration of the body:"))
    t1 = int(input("time period"))
    v1 = u1 + a1*t1
    return v1

def motion2():
    u2 = int(input("initial velocity:"))
    a2 = int(input("acceleration of the body:"))
    t2 = int(input("time period"))
    s1 = u2*t2 + (1/2)*(a2)*(t2**2)
    return s1

def motion3():
    u3 = int(input("initial velocity:"))
    a3 = int(input("acceleration of the body:"))
    s2 = int(input("distance travelled:"))
    v2 = ((u3**2) + 2*a3*s2)**(0.5)
    return v2

def average_acc():
    v3_1 = int(input("enter initial velocity:"))
    v3_2 = int(input("enter final velocity:"))
    t_1 = int(input("enter initial time:"))
    t_2 = int(input("enter final time:"))
    avg_a = (v3_2-v3_1)/(t_2-t_1)
    return avg_a

def rel_vel():
    v4_1 = int(input("enter the initial velocity:"))
    v4_2 = int(input("enter the final velocity:"))
    del_v = v4_2-v4_1
    return del_v 

#####################################
#####################################







#addition, deletion and modification dataframe!!



########################
########################

