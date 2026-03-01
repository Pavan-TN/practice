string = input("Enter a string: ")

if string.isalpha():
    print("String contains only alphabets")

elif string.isalnum():
    print("String contains alphabets and numbers")

else:
    print("String contains special characters")