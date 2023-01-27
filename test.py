x = int(input("How old are you? "))
y = 2023 - x
mob = 0
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

print("You were born in " + str(y))
z = int(input("In an ascending ranking of Months i.e 1-12, Your month is ? "))

if z == 1:
    mob = months[0]
elif z == 2:
    mob = months[1]
elif z == 3:
    mob = months[2]
elif z == 4:
    mob = months[3]
elif z == 5:
    mob = months[4]
elif z == 6:
    mob = months[5]
elif z == 7:
    mob = months[6]
elif z == 8:
    mob = months[7]
elif z == 9:
    mob = months[8]
elif z == 10:
    mob = months[9]
elif z == 11:
    mob = months[10]
elif z == 12:
    mob = months[11]
print("That's " + str(mob))

day = str(input("On what day, precisely? "))

print(str(day) + " " + str(mob) + " " + str(y) + " " + "is an amazing day to be born")
print("Now you know your Date of Birth")
