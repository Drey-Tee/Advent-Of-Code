import re

col ="""TRGWQMFP
RFH
DSHGVRZP
GWFBPHQ
HJMSP
LPRSHTZM
LMNHTP
RQDF
HPLNCSD"""

with open("input.txt", "r") as f:
    data = f.read()

out = 0

initial, instructions = data.split('\n\n')
crates = [list(l) for l in col.splitlines()]

for l in instructions.split('\n'):
    n, x, y = map(int, re.findall(r'\d+', l))
    x -= 1
    y -= 1
    to_move = crates[x][:n]
    crates[x] = crates[x][n:]
    crates[y] = to_move + crates[y]

results = ""
for i in range(len(crates)):
    if len(crates[i]):
        results += crates[i][0]

print(results)