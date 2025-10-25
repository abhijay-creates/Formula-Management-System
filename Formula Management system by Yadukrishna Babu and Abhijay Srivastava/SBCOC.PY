import ChemistryFunctions 

while True:
    print("__________[SOME BASIC CONCEPTS OF CHEMISTRY FORMULAES]___________")
    print("|__F1______|________________M=n/V________________________________|")
    print("|__F2______|________________M%=(m1/m2)*100_______________________|")
    print("|__F3______|_________________k=C+273.15__________________________|")
    print("|__F4______|_________________N=V/22.4____________________________|")
    print("|__F5______|_________________F=(9/5)C+32_________________________|")

    f=input("\nwhich formula do you want to use?:")
    if f=='F1':
        print(ChemistryFunctions.molarity())
    elif f=='F2':
        print(ChemistryFunctions.masspercent())    
    elif f=='F3':
        print(ChemistryFunctions.tempkc())
    elif f=='F4':
        print(ChemistryFunctions.stp())
    elif f=='F5':
        print(ChemistryFunctions.tempfc())
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