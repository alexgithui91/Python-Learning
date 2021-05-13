# Modifying values and keys
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25, 'grapes': 0.80}

for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)

# print(prices)

for key in list(prices.keys()):
    if key == "banana":
        del prices[key]

# print(prices)

# turn keys into values and vice versa
new_dict = {}

for k, v in prices.items():
    new_dict[v] = k

# print(new_dict)

another_dict = {}

for k, v in prices.items():
    if v > 0.35:
        another_dict[k] = v

print(another_dict)
