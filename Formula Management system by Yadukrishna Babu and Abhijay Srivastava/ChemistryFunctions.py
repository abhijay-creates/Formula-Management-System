#________________________atomic structure formulaes__________________________
def ENERGY1():
    m=float(input("enter a value of m(mass):"))
    c=float(input("enter the speed of light:"))
    E=m*(c**2)
    return("The Energy is",E,"joules")

def ENERGY2():
    h=6.62607015*10**(-34)
    v=float(input("enter frequency value in (Hz)"))
    E=h*v 
    return("The Energy is:",E) 

def TOTALSPIN():
    while True:
     try:
       n=int(input("enter the number of unpaired electrons:"))
       s=n*(1/2)
       break 
     except ValueError:
         print("---------------------------------")
         print("|*************ERROR!!!**********|")
         print("|please select an integer value.|")
         print("|_______________________________|") 
    return("the total spin of electrons:",s)

def NOOFELECTRON():
    while True:
     try:
       n=int(input("enter the principal quatum number value:"))
       S=2*(n**2)
       break 
     except ValueError:
         print("---------------------------------")
         print("|*************ERROR!!!**********|")
         print("|please select an integer value.|")
         print("|_______________________________|") 
    return("the number of electrons is",S) 

def SPIN():
    while True:
        try:
         n=int(input("enter the number of unpaired electron(integer only):")) 
         u=(n*(n+2))**(1/2)
         break
        except ValueError:
         print("---------------------------------")
         print("|*************ERROR!!!**********|")
         print("|please select an integer value.|")
         print("|_______________________________|")       
    return("the spin magnetic moment of the given element is:",u)
 
#___________________________________________________________________________    
#___________________________Gaseous State___________________________________ 
def PVnrt():
   Vint=float(input("enter the value of volume(M^3):"))
   Tint=float(input("enter the value of temperature(Kelvin):")) 
   r=8.314 
   nint=float(input("enter the number of moles:")) 
   pint=(nint*r*Tint)/Vint 
   return("the pressure in pascal is:",pint,"Pa")  

def rms():
   k=1.380649*(10**(-23)) 
   m=float(input("enter the mass of gas:"))
   t=float(input("enter the temperature:"))
   rms=((3*k*t)/m)**(0.5) 
   return("the rms velocity of the gas is:",rms,"m/s") 

def av():
   k=1.380649*(10**(-23)) 
   m=float(input("enter the mass of gas:"))
   t=float(input("enter the temperature:"))
   av=((8*k*t)/(3.14*m))**(0.5) 
   return("the average velocity of the gas is:",av,"m/s")  

def ump(): 
   k=1.380649*(10**(-23)) 
   m=float(input("enter the mass of gas:"))
   t=float(input("enter the temperature:"))
   ump=((2*k*t)/(3.14*m))**(0.5) 
   return("the most probable velocity of the gas is:",ump,"m/s")   

def KE():
   r=8.314 
   nint=float(input("enter the number of moles:")) 
   Tint=float(input("enter the value of temperature(Kelvin):")) 
   KE=(1.5)*nint*r*Tint 
   return("the kinetic energy of the gas is:",KE,"J")  
#____________________________________________________________________________________________    
#_________________________________________SBCOC___________________________________________# 
def molarity():
   n=float(input("enter the number of moles:")) 
   v=float(input("enter the voloume in litres:")) 
   Molarity=n/v 
   return("the molarity of the substance is:",Molarity) 

def masspercent():
   m1=float(input("enter the mass of the solute:")) 
   m2=float(input("enter the mass of the solution:")) 
   mper=(m1/m2)*100 
   return("the mass percent of the given solute in the solution is-",mper,"%") 

def tempkc():
   temp=float(input("enter the temperature in degree celcius:"))
   k_c=temp+273.15 
   return "the temperature in kelvin is:",k_c 

def stp():
   vstp=float(input("enter the volume of gas at STP:"))
   nstp=(vstp/22.4) 
   mstp=nstp*(6.02214076*(10**(23))) 
   print("the number of moles of the gas is: ",nstp,"moles") 
   return "the number of molecules of the gas is:",mstp ,"molecules"

def tempfc():
   temp=float(input("enter the temperature in degree celcius:"))
   f_c=(9/5)*temp+32 
   return("the temperature in fahrenhiet is:",f_c,"fahrenhiet")    

       
   
   

   

   

