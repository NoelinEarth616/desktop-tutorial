#Q1
num = int(input("Enter value: "))
def sum_cal(num):
    tong = 0
    for i in range(1, num+1):
        tong = tong + i
        
    print(f"The sum is : {tong}")

sum_cal(num)


#Q2
arr = [int(x) for x in input("Enter values for a list seperated by whitespace: ").split()]
for i in arr:
    if i>500:
        print("Number is larger than 500.")
        break
    if i>150:
        print(f"{i} is larger than 150")
        continue
    if i<=150 and i%5 == 0:
        print(i)
    def digit_count(i):
        num_str = str(i)
        digits = len(num_str)
        print(f"Total number of digits: {digits}")
    digit_count(i)  
num_list = [1, 2 ,3 ,4 ,5]
rev = len(num_list) -1
while rev>=0:
    print(num_list[rev])
    rev -= 1    

