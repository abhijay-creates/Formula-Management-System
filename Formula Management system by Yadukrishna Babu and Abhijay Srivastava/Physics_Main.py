import os
import subprocess

while True:
    while True:
        print("1. MECHANICS")
        print("2. HEAT TRANSFER")
        print("3. ELECTROSTATICS")
        print("4. YOUR FORMULA SHEET")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subprocess.call(["python", "MECHANICS.py"])
        elif choice == "2":
            subprocess.call(["python", "HEAT TRANSFER.py"])
        elif choice == "3":
            subprocess.call(["python", "ELECTROSTATICS.py"])
        elif choice == "4":
            subprocess.call(["python", "dataframe.py"])
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5")
    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")