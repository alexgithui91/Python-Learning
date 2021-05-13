a_dict = {
    "singer": "whitney houston",
    "dancer": "chris brown",
    "artist": "basquiat",
    "rapper": "lil wayne"}

# Way to loop through dict
print("method 1 : ")
for key in a_dict:
    print(key + " --> " + a_dict[key])

# Another way 
print("method 2 : ")
for item in a_dict.items():
    print(item) # returns a tuple

# Yet another way
print("method 3 : ")
for key, value in a_dict.items():
    print(key, "----->", value)