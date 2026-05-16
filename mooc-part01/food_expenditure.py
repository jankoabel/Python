meals = int(input("How many times a week do you eat at the student cafeteria? "))
meal_cost = float(input("The price of a typical meal? "))
grocery_cost = float(input("How much money do you spend on groceries in a week? "))
weekly = meals * meal_cost + grocery_cost
daily = weekly / 7
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
