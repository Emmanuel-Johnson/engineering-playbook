from collections import Counter

string = "programming"

count = Counter(string)

sorted_count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

print(sorted_count)