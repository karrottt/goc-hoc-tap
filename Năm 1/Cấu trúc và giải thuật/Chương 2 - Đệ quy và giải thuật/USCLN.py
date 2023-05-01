import math

def ucln(a, b):
    ucln = math.gcd(a, b)
    print("\nƯớc số chung lớn nhất của", a, "và", b, "là:", ucln)

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

ucln(a, b)
