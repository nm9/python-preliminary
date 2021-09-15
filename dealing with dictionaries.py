#information stored in the form of key, value pairs

monthConversions = {
    "Jan": "January",                #Unique keys compulsory, in key : value pairs
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Blub"))
print(monthConversions.get("Blub", "Not a valid key"))
