from string import ascii_lowercase, ascii_uppercase

with open("input.txt", "r") as f:
    data = f.read()

output = 0

for i in data.split("\n"):
    string1 = i[:len(i) // 2]
    string2 = i[len(i) // 2:]

    assertion = set(string1).intersection(set(string2))

    for k in assertion:
        if k in ascii_lowercase:
            output += ascii_lowercase.index(k) + 1
        elif k in ascii_uppercase:
            output += ascii_uppercase.index(k) + 27

print(output)