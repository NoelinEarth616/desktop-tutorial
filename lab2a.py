
print("ý 1.1")
def func1(a,b,c):
    print("Printing Values")
    print(a)
    print(b)
    print(c)
func1(20,40,60)

def func2(d,e):
    print("Printing Values")
    print(d)
    print(e)
func2(80,100)

print("ý 1.2")
def calculation(a, b):
    a = a + 10
    b = b + 20
    return a, b

res = calculation(40, 10)
print(res)

print("ý 2.1")
def showEmployee(a, salary = 9000):
    print(f"Name : {a}, Salary : {salary}")

showEmployee("Ben", 12000)
showEmployee("Jessa")

print("ý 2.2")
def outer_fun(a,b):
    tong = a + b
    tong = tong + 5
    return(tong)
result = outer_fun(5,10)
print(result)

print("ý 3.1")
def addition(n):
    sum = (n*(n+1))/2
    print(sum)
res = addition(10)
print(res)

print("ý 3.2")
def display_student(a, age):
    print(f"{a}, {age}")
def show_student(a, age):
    print(f"{a}, {age}")
display_student("Emma", 26)
show_student("Emma", 26)

print("ý 3.3")
def find_largest_number(numbers):
    if not numbers:
        return None  
    return max(numbers)
x = [4, 6, 8, 24, 12, 2]
print(find_largest_number(x))

print("ý 4")
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")