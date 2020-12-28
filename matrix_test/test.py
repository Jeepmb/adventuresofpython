#!/usr/bin/python3
usr_choice = int(input("What number would you like to search for?:"))

index = [1,2,3,4,5]

matrix = [
        [1,2,3,4,5],
        [6,7,8,9,0]
        ]

print(matrix)

print("Does this code recognise the presence of this item in the matrix?: " + str(any(usr_choice in sub for sub in matrix)))

print([(index, row.index(usr_choice)) for index, row in enumerate(matrix) if usr_choice in row])
