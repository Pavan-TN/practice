a = int(input("enter the numbers"))
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a //= 10
print(rev)    