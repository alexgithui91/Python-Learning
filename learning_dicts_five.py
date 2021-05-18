# removing specific items from dict

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}

non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}

print(non_citric)