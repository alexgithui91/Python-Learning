# Doing some calculations

incomes = {
    "alex": 5000,
    "peter": 1000,
    "drake": 7000,
    "paul": 1500,
    "lamelo": 9000}

total_income = 0.0

for value in incomes.values():
    total_income += value

# print("total income:", total_income)

# using comprehension
first_name = [
    "Lebron",
    "Dwyane",
    "Carmelo",
    "Lamelo",
    "James",
    "Michael",
    "Shaquile"]
last_name = [
    "James",
    "Wade",
    "Anthony",
    "Ball",
    "Harden",
    "Jordan",
    "O'neil"]

sports_dict = {key: value for key, value in zip(first_name, last_name)}

# print(sports_dict)

# turning keys into values revisited
new_sports_dict = {value: key for key, value in sports_dict.items()}

# print(new_sports_dict)

# filter items revisited
filtered_sports_dict = {
    key: value for key,
    value in sports_dict.items() if len(key) >= 7}

print(filtered_sports_dict)

# doing some calculations revisited

profits = {"bus_one": 1500, "bus_two": 1000, "bus_three": 500, "bus_four": 500}

total_profits = sum(profits.values())

print(total_profits)
