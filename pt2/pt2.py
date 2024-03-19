
print("Q1")
def replace_char(s, c1, c2):
    new_s = ""

    for char in s:
        if char == c1:
            char = c2
        new_s += char

    return new_s

s = input("Enter a string (no spaces): ")

c1 = input("Enter the first character: ")
c2 = input("Enter the second character: ")

result = replace_char(s, c1, c2)

print("Result: ", result)

print("Q3")
def max_value(N, W, items):
    memo = [0] * (W + 1)
    for i in range(N):
        for w in range(W, -1, -1):
            if w >= items[i][0]:
                memo[w] = max(memo[w], memo[w - items[i][0]] + items[i][1])
    return memo[W]

def print_sol(N, W, items, memo):
    k = W
    res = []
    for i in range(N - 1, -1, -1):
        if memo[W] == memo[W - items[i][0]] + items[i][1]:
            res.append((items[i][2], W // items[i][0]))
            W -= items[i][0] * (W // items[i][0])
    return res

with open('BAG.INP', 'r') as f:
    N, W = map(int, f.readline().strip().split())
    items = []
    for i in range(N):
        g, vi, ni = map(int, f.readline().strip().split())
        items.append((g, vi, ni))

memo = [0] * (W + 1)
max_value = max_value(N, W, items)
print('Maximum value found:', max_value)

res = print_sol(N, W, items, memo)
for i in res:
    print(i[1], i[0])