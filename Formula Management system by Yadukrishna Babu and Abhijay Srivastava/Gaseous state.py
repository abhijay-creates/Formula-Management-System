import ChemistryFunctions 

while True:
    print("__________[GASEOUS STATE FORMULAES]___________")
    print("|__F1______|______PV=nRT_____________________|")
    print("|__F2______|______Urms=(3kt/m)^1/2___________|")
    print("|__F3______|______Uav=(8kt/πm)^1/2___________|")
    print("|__F4______|______Ump=(2kt/πm)^1/2___________|")
    print("|__F5______|______Kinetic energy=1.5nRT______|")

    f=input("\nwhich formula do you want to use?:")
    if f=='F1':
        print(ChemistryFunctions.PVnrt())
    elif f=='F2':
        print(ChemistryFunctions.rms())    
    elif f=='F3':
        print(ChemistryFunctions.av())
    elif f=='F4':
        print(ChemistryFunctions.ump())
    elif f=='F5':
        print(ChemistryFunctions.KE())
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