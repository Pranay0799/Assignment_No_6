## 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.


import json


IndianStates_Capitals = {
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Kerala" : "Thiruvananthapuram",
    "Punjab": "Chandigarh",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "West Bengal": "Kolkata"
}

with open(r"IndianStates.json","w") as file:      ####provide_path
    json.dump(IndianStates_Capitals, file)



###### Thank You....