with open("input.txt","r") as f:
    grid = [list(map(int, line)) for line in f.read().splitlines()]
    max_score = float("-inf")
    sees = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            score = 1
            see = False
            c = grid[y][x]

            for i in range(x + 1, len(grid[0])):
                if grid[y][i] >= c:
                    score *= i - x
                    break
            else:
                score *= len(grid[0]) - 1 - x
                see = True

            for i in range(x - 1, -1, -1):
                if grid[y][i] >= c:
                    score *= x - i
                    break
            else:
                score *= x
                see = True

            for i in range(y + 1, len(grid)):
                if grid[i][x] >= c:
                    score *= i - y
                    break
            else:
                score *= len(grid) - 1 - y
                see = True

            for i in range(y - 1, -1, -1):
                if grid[i][x] >= c:
                    score *= y - i
                    break
            else:
                score *= y
                see = True

            max_score = max(max_score, score)
            if see:
                sees += 1

    print("Treetop Treehouse Part 1:", sees)
    print("Treetop Treehouse Part 2:", max_score)