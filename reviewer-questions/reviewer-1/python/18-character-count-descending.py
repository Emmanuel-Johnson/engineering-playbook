string = "programming"

count = {}

for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

sorted_count = dict(
    sorted(count.items(), key=lambda x: x[1], reverse=True)
)

print(sorted_count)