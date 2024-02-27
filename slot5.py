largest_so_far = -1 
for i in [999, 4451, 8892, 7753, 7334, 1225]:
    if i > largest_so_far:
        largest_so_far = i
print(largest_so_far)

count = 0
sum = 0
for a in [999, 4451, 8892, 7753, 7334, 1225]:
    count = count + 1
    sum = a + sum
avg = sum / count
print(avg)

smallest_so_far = None
for i in [999, 4451, 8892, 7753, 7334, 1225]:
    if smallest_so_far == None:
        smallest_so_far = i
    if i < smallest_so_far:
        smallest_so_far = i
print(smallest_so_far)

tong = 0
n = int(input("nhập n: "))
for t in range(1,n+1):
    tong = tong + t
print(f"tổng là {tong}")