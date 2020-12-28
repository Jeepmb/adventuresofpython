#!/usr/bin/python3

usr_choice = input("What bar would you like to know about?:")

bars = [
        ["Manito",3,6,"All",],
        ["Republic",4,6,"Monday"]
        ]

y_pos = bars.index(usr_choice)

start_time = bars[y_pos][1]
end_time = bars[y_pos][2]

if usr_choice in bars:
    print(usr_choice + " is open for happy hour from " + start_time + " to " + end_time)
else:
    print("Not located in database!")
