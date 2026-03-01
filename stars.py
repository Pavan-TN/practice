rows = int(input("enter the rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()  
 
  
# for i in range(rows):
#     for j in range(i,rows):
#         print("*",end=" ")
#     print()    


# for i in range(rows):
#     for j in range(i,rows):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*",end=" ")    
#     print()    
        
        
# for i in range(rows):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,rows):
#         print("*", end=" ")
#     print()    

# for i in range(rows):
#     for j in range(i,rows):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     for m in range(i+1):
#         print("*",end=" ")
#     print()   

         
# for i in range(rows):
#     for j in range(i+1):
#         print(" ", end= " ")
#     for k in range(i,rows-1):
#         print("*",end=" ")    
#     for m in range(i,rows):
#         print("*",end=" ")   
#     print()     



# for i in range(rows-1):
#     for j in range(i,rows):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     for m in range(i+1):
#         print("*",end=" ")
#     print()   
# for i in range(rows):
#     for j in range(i+1):
#         print(" ", end= " ")
#     for k in range(i,rows-1):
#         print("*",end=" ")    
#     for m in range(i,rows):
#         print("*",end=" ")   
#     print()  


# for i in range(rows):
#     for j in range(rows - i -1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         if k == 0 or k == 2 * i:
#             print("*",end =" ")    
#         else:
#             print(" ", end=" ")
#     print()            
# for i in range(rows -2,-1,-1):
#     for j in range(rows - i -1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         if k == 0 or k == 2 * i:
#             print("*",end =" ")    
#         else:
#             print(" ", end=" ")
#     print()    
    
    
# for i in range(rows):
#         for j in range(rows -i -1):
#             print(" ",end=" ")  
#         for k in range(2 * i + 1):
#             if i == 0 or i == rows-1:
#                 print("*", end=" ")
#             else:
#                 if k == 0 or k == 2 * i:
#                     print("*",end=" ")
#                 else:
#                     print(" ",end=" ")
#         print() 


# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * (rows - i)):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")  
#     print()

# for i in range(rows, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * (rows - i)):
#         print(" ", end=" ")   
#     for j in range(i):
#         print("*", end=" ")
    
#     print()   


# num = 1
# for i in range(1,rows + 1):
#     for j in range(i):
#         print(num,end=" ")      
#         num = num + 1
#     print()


# for i in range(1,rows + 1):
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print()                  
                    
                    
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")     
    print((str(i) + " ") * i)         

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")      
    print((str(i) + " ") * i)                          
                              