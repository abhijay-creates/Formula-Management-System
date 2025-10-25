import Physics_Functions


 
while True:
    print("________________________[ELECTROSTATICS FORMULAS]___________")
    print("|__F1______|______QUANTIZATION_____________________________|")
    print("|__F2______|______RELATIVE PERMEABILITY____________________|")
    print("|__F3______|______COLOUMB'S LAW____________________________|")
    print("|__F4______|______ELECTRIC FIELD___________________________|")
    print("|__F5______|______ELECTRIC FLUX____________________________|")





    f = input("enter formula :- ")

    if f == 'F1':
        print(Physics_Functions.quantization())

    elif f == 'F2':
        print(Physics_Functions.relative_permeability())

    elif f == 'F3':
        print(Physics_Functions.coulomb_law())

    elif f == 'F4':
        print(Physics_Functions.electric_field())

    elif f == 'F5':
        print(Physics_Functions.electric_flux())

    else:   
        print("Wrong Input")

    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")





