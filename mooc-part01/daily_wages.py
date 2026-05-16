wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    total = wage * hours * 2
else:
    total = wage * hours
print(f"Daily wages: {total} euros")
