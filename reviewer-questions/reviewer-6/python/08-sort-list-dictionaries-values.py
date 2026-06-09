students = [
    {"name": "John", "age": 20},
    {"name": "Anna", "age": 18},
    {"name": "Mike", "age": 22}
]

print(sorted(students, key = lambda x: x["age"]))


# Bubble sort
for i in range(len(students)):
    for j in range(len(students) - 1 - i):
        
        if students[j]["age"] > students[j + 1]["age"]:
            
            # swap
            students[j], students[j + 1] = students[j + 1], students[j]

print(students)