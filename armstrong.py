num = int(input("enter the number")) # taking the user input
original = num                       #variable
sum = 0
n = len(str(num))                    #find the length
while num >0:                        #looping
    digit = num % 10                 # logic
    sum += digit ** n
    num //= 10
if sum == original:
    print("armstrong") 
else:
    print("not")       