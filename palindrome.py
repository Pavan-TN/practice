string = input("Enter a string: ")  #taking the string from the user
reverse = ""                        #initially the reverse value is null
for ch in string:                   # using for loop for iteration
    reverse = ch + reverse          # add letters to variable

if string == reverse:               # check both r true
    print("Palindrome")             # true 
else:
    print("Not Palindrome")         #falseS