student = {
    "name": "John",
    "scores": [80, 90, 100]
}

student["scores"] = sum(student["scores"]) / len(student["scores"])

print(student)