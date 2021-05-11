# One way to define a dict
basketball_teams = {
    "Houston": "Rockets",
    "Dallas": "Mavericks",
    "Los Angeles": "Lakers",
    "Detroit": "Pistons",
    "New York": "Knicks"
}

# Another way to define a dict
cars = dict([
    ("Toyota", "Landscruiser"),
    ("VW", "Beetle"),
    ("BMW", "M3"),
    ("Ferrari", "Enzo"),
    ("Mercedes Benz", "E200")]
)

# Yet another way to define a dict
mlb_teams = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

# Print dict item
print(basketball_teams["Houston"])

# Add to dict
cars["Mazda"] = "Demio" 
print(cars)

# Delete an item from dict
del mlb_teams["Seattle"]
print(mlb_teams)
