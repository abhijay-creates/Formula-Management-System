import Physics_Functions



while True:
    print("________________________[MECHANICS FORMULAS]______________________")
    print("|__F1______|______NEWTON'S LAW OF MOTION-1_______________________|")
    print("|__F2______|______NEWTON'S LAW OF MOTION-2_______________________|")
    print("|__F3______|______NEWTON'S LAW OF MOTION-3_______________________|")
    print("|__F4______|______AVERAGE ACCERATION_____________________________|")
    print("|__F5______|______RELATIVE VELOCITY______________________________|")



    f = input("enter formula :- ")

    if f == 'F1':
        print(Physics_Functions.motion1())

    elif f == 'F2':
        print(Physics_Functions.motion2())

    elif f == 'F3':
        print(Physics_Functions.motion3())

    elif f == 'F4':
        print(Physics_Functions.average_acc())

    elif f == 'F5':
        print(Physics_Functions.rel_vel())
    else:
        print("Wrong Input")
    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        
