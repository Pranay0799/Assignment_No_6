#### 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.

import json

class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name}, {self.dob}, {self.height}, {self.city}, {self.state}"
    
with open(r"employee.json", "r") as file:     ####provide_path
    e_data = json.load(file)

employees =[]

for emp in e_data["employees"]:
   employees.append(Employee(emp["name"], emp["dob"], emp["height"], emp["city"], emp["state"]))


for employee in employees:
    print(employee)





###### Thank You....