import os
import subprocess

while True:
    while True:
        print("1. Some basic concepts of chemistry")
        print("2. Gaseous State")
        print("3. Atomic Structure")
        print("4. Chemsitry Formula table") 
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subprocess.call(["python", "SBCOC.py"])
        elif choice == "2":
            subprocess.call(["python", "Gaseous state.py"])
        elif choice == "3":
            subprocess.call(["python", "Atomic structure.py"]) 
        elif choice == "4":
            subprocess.call(["python", "ChemsitryFormula_table.py"])    
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 OR 5")
    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")