# class Bank:
    
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def show(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)


# name = input("Enter Account Holder Name: ")
# balance = int(input("Enter Balance: "))

# b1 = Bank(name, balance)
# b1.show()



# class Addition:
    
#     def add(self, a, b):
#         result = a + b
#         print("Sum =", result)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# obj = Addition()
# obj.add(num1, num2)




# class Bank:
    
#     def __init__(self, balance):
#         self.__balance = balance   # private variable

#     def show_balance(self):
#         print("Balance =", self.__balance)


# # User input
# b = int(input("Enter Balance: "))
# obj = Bank(b)
# obj.show_balance()




# class Prime:
    
#     def check(self, num):
#         count = 0

#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count = count + 1

#         if count == 2:
#             print("Prime Number")
#         else:
#             print("Not a Prime Number")

# # User input
# n = int(input("Enter a number: "))
# obj = Prime()
# obj.check(n)



class EvenOdd:
    
    def check(self, num):
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")


# User input
n = int(input("Enter a number: "))
obj = EvenOdd()
obj.check(n)