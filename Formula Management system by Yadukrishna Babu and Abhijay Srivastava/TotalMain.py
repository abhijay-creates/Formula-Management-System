import os
import subprocess

while True:
    while True:
        print("1. Physics")
        print("2. Chemistry")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subprocess.call(["python", "Physics_Main.py"])
        elif choice == "2":
            subprocess.call(["python", "ChemistryMain.py"])
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, OR 3.")
    answer = input("Do you want to run the program again? (y/n): ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")