#!/usr/bin/python3

usr_choice = input("What bar would you like to know about?:\n")

bars = [
        ["Manito Taphouse","3","6","All",],
        ["Republic Pi","4","6","Monday"]
        ]

end = ""

for element in bars:
    for sub_element in element:
        if usr_choice in sub_element:
            print(sub_element)
            start = element[1]
            end = element[2]
            print("The happy hour for " + usr_choice + " is from " + start + " to " + end)

if end == "":
    print("That bar is not yet listed in our database")
