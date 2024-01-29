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

#Q3
def mixed_string(string):
    middle_len = len(string) // 2
    middle_four = string[middle_len - 2 : middle_len + 2]
    mixed_str =  middle_four
    return mixed_str
str1 = str(input("Enter string: "))
res = mixed_string(str1)
print(f"Original string: {str1}")
print(f"Middle four are: {res}")
def appen_str(string1, string2):
    mid_len = len(string1) // 2
    string3 = string1[:mid_len] + string2 + string1[mid_len:]
    return string3
str1 = 'ab'
str2 = 'cd'
res = appen_str(str1, str2)
print(res)
def mixed_str_create(string1, string2):
    mid_len_string1 = len(string1)// 2
    mid_len_string2 = len(string2)// 2
    mixed_str1n2 = string1[0] + string2[0] + string1[mid_len_string1] + string2[mid_len_string2] + string1[-1] + string2[-1]
    return mixed_str1n2
str1 = 'America'
str2 = 'Japan'
res_mixed = mixed_str_create(str1, str2)
print(res_mixed)
new_str_lower = ''
new_str_upper = ''
new_str =''
string1 = str(input("Enter string: "))
for char in string1:
    if char == char.lower():
        new_str_lower = new_str_lower + char  
    if char == char.upper():
        new_str_upper = new_str_upper + char
    new_str = new_str_lower + new_str_upper    
print(new_str)      
string = str(input("Enter string: "))
new_string = string.replace(" ", "")
spc_count = 0
int_count = 0
nrm_count = 0
for char in string:
    if char.isalnum() == False:
        spc_count +=1
print(spc_count)
for i in string:
    number_lis = '0123456789'
    if i in number_lis:
        int_count +=1
print(int_count)
nrm_count = nrm_count + len(string) - int_count - spc_count
print(nrm_count)
