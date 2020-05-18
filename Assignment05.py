# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# APaulson,5.17.20,Added code to complete assignment05
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
strFile = "ToDoList.txt"  # File Name
lstData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A capture the user option selection

# Define menu of user options
strMenu = """    
    Menu of Options    
    1) Show current data    
    2) Add a new item.    
    3) Remove an existing item.    
    4) Save Data to File    
    5) Exit Program    """

# Add items to ToDoList.txt
objFile = open(strFile, "w")
dicRow = {"Task": "Water Plants", "Priority": "High"}
objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + '\n')
dicRow = {"Task": "Sweep", "Priority": "Low"}
objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + '\n')
objFile.close()

# -- Processing -- #
# Step 1 - When the program starts, load text file called ToDoList.txt into a python list of dictionaries
objFile = open(strFile, "r")
for row in objFile:
    lstData = row.split(",")  # Returns row as a list
    dicRow = {"Task": lstData[0].strip(),
              "Priority": lstData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print("Task: " + row.get("Task") + ", Priority: " + row.get("Priority"))
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("Please enter a task: ")
        strPriority = input("Please enter a priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        removeChoice = input("Please enter the task you would like to remove: ")
        for i in range(len(lstTable)):
            if lstTable[i]['Task'] == removeChoice:
                print("Task: " + lstTable[i]["Task"] + ", Priority: " + lstTable[i]["Priority"] + ", has been removed.")
                del lstTable[i]
            break
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        print("Your tasks have been saved to the file.")
        for row in lstTable:
            objFile.write(row.get("Task") + ", " + row.get("Priority") + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Thank you for using the program!")
        break  # and Exit the program
