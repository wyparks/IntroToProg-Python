# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# WParks,14May2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
import os  # Using os to check if initial txt file is empty to avoid adding an empty dictionary to the table
objFile = None
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:  # using try-except for if file is not already made
    objFile = open(strFile, 'r')
    if os.path.getsize(strFile) == 0:  # using getsize to avoid empty dictionary in list
        objFile.close()
    else:
        for i in objFile:  # separating values in txt file into list, then dictionary, then list of dictionaries
            lstRow = i.strip().split(',')
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
    objFile.close()
except FileNotFoundError:  # if new file needs to be generated
    objFile = open(strFile, 'w')
    objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:  # if no data in file
            print('Please add data :)')
        else:  # loop through table and return values
            print('Current Data:')
            for i in lstTable:
                print(f"{i['Task']}, {i['Priority']}")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print('Entering new task to list\n')
        strTask = input('Enter Task: ')
        strPrio = input('Enter priority of task: ')
        dicRow = {"Task": strTask, "Priority": strPrio}
        lstTable.append(dicRow)
        print(f'{strTask} with priority: {strPrio} has been added to the list')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeItem = input('Input the task you would like to remove: ')  #
        for i in lstTable:
            if i['Task'].lower() == removeItem.lower():
                lstTable.remove(i)
        print(f'Removed {removeItem} from list')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, 'w')
        for i in lstTable:
            objFile.write(i["Task"] + ',' + i["Priority"] + "\n")
        objFile.close()
        print('List saved to file')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        Print('Ending program')
        break  # and Exit the program
