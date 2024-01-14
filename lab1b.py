import math
#ý a)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
x = int(input("Nhập x: "))

#ý b)
S1 = a*x**2+b*x+c
print("Tổng S1 là:", S1)

#ý c)
beforeS2 = b**2 - 4*a*c
if beforeS2 > 0:
    S2 = (b**2 - 4*a*c)^(1/2)
    print("S2 là: ",S2)
elif beforeS2 < 0:
    print("Không tìm được S2")
else:
    print("S2 là: ",beforeS2)

#ý d)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

bdt = a + b - c
if bdt > 0:
    print("a, b, c là độ dài 3 cạnh của một tam giác")
else:
    print("a, b, c không phải độ dài 3 cạnh của một tam giác")

def heron(a, b, c):
    p = (a + b + c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"The area is {area}")

heron(a, b, c)
chuvi = p * 2
print("Chu vi là: ",chuvi)

