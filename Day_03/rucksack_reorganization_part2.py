from string import ascii_lowercase, ascii_uppercase

with open("input.txt", "r") as f:
    data = f.read()

output = 0

data = data.split("\n")
for i in range(0, len(data), 3):
    shared = set(ascii_lowercase).union(set(ascii_uppercase))
    for j in range(i, i + 3):
        shared = shared.intersection(set(data[j]))

    for x in shared:
        if x in ascii_lowercase:
            output += ascii_lowercase.index(x) + 1
        elif x in ascii_uppercase:
            output += ascii_uppercase.index(x) + 27

print(output)