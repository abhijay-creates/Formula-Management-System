import ChemistryFunctions 
   
while True:
    print("__________[ATOMIC STRUCTURE FORMULAES]_________")
    print("|__F1______|______E=mc^2______________________|")
    print("|__F2______|______E=hv________________________|")
    print("|__F3______|______s=n*(1/2)___________________|")
    print("|__F4______|______NO. OF E-=2n^2______________|")
    print("|__F5______|______SPINMAG=spin=(n(n+2))^1/2___|")

    f=input("\nwhich formula do you want to use?:")
    if f=='F1':
        print(ChemistryFunctions.ENERGY1())
    elif f=='F2':
        print(ChemistryFunctions.ENERGY2())    
    elif f=='F3':
        print(ChemistryFunctions.TOTALSPIN())
    elif f=='F4':
        print(ChemistryFunctions.NOOFELECTRON())
    elif f=='F5':
        print(ChemistryFunctions.SPIN())
    else:
        print("-----------------------------------")
        print("|*************ERROR!!!************|")
        print("|please select the proper formula.|")
        print("|_________________________________|")
    
    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")