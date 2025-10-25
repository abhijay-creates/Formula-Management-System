import Physics_Functions





while True:

    print("________________________[HEAT TRANSFER FORMULAS]_______________________________")
    print("|__F1______|______EMMISIVE POWER = ENERGY ABSORBED/GIVEN OUT__________________|")
    print("|__F2______|______HEAT CHANGE = Δθ*K*A*t/l____________________________________|")
    print("|__F3______|______THERMAL R = Δθ/H____________________________________________|")
    print("|__F4______|______R(Equivalent)(PARALLEL)= R1*R2/R1+R2________________________|")
    print("|__F5______|______TEMPERATURE GRADIENT = ΔT/Δx________________________________|")


    f = input("enter formula :- ")

    if f == 'F1':
        print(Physics_Functions.emmisivepower())

    elif f == 'F2':
        print(Physics_Functions.heatchange())

    elif f == 'F3':
        print(Physics_Functions.thermal_res())

    elif f == 'F4':
        print(Physics_Functions.equivalent_res_parll())

    elif f == 'F5':
        print(Physics_Functions.temp_gradient())

    else:   
        print("Wrong Input")

    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")








    
