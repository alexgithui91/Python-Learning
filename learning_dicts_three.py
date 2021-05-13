# Modifying values and keys
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25, 'grapes': 0.80}

for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)

# print(prices)

for key in list(prices.keys()):
    if key == "banana":
        del prices[key]

print(prices)