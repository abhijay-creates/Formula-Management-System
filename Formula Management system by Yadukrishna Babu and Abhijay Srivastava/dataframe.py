import pandas as pd
df = pd.DataFrame(columns=[' About Formula', 'Formula', 'Notes:'])


while True:
    name = input("Enter something about the formula (or 's' to save): ")
    if name == 's':
        break
    formula = input("Enter formula: ")
    notes = input("Enter description: ")

    
    df = df.append({' About Formula': name, 'Formula': formula, 'Notes:': notes}, ignore_index=True)      
print("TABLE SUCCESSFULLY CREATED!")  
print(df)
print("_______________________[Commands]______________________")
print("|__M______|__________To modify the table______________|")
print("|__V______|____________View the table_________________|")
print("|__D______|______To delete elements in the table______|")

userinp=input("what do you want to use?")

if userinp=='M':
 while True:
     index = input("Enter index of formula to modify (or 's' to save): ")
     if index == 's':
        break
     name = input("Enter new About Formula: ")
     formula = input("Enter new Formula: ")
     description = input("Enter new Notes: ")

    # Modify the data in the DataFrame
     df.loc[int(index), ' About Formula'] = name
     df.loc[int(index), 'Formula'] = formula
     df.loc[int(index), 'Notes:'] = description 

elif userinp=='V':
   print(df)    
 
     
elif userinp=='D':
   while True:
    index = input("Enter index of formula to delete (or 'q' to quit): ")
    if index == 'q':
        break

    # Delete the data from the DataFrame
    df = df.drop(int(index))  
    
    print(df)

else:
   print("-----------------------------------")
   print("|*************ERROR!!!************|")
   print("|please select the proper command.|")
   print("|_________________________________|")    
