# Single Inheritance
# class Father:
#     def show_father(self):
#         print("This is Father class")

# class Son(Father):
#     def show_son(self):
#         print("This is Son class")

# obj = Son()

# obj.show_father()
# obj.show_son()

# multi level
# class department:
#     def cse(self):
#         print("computer science department")
# class sub_department(department):
#     def ds(self):
#         print("data science") 
# class sub_department1(sub_department):
#     def IS(self):
#         print("information science")               
        
# D=sub_department1()
# D.cse()
# D.ds()
# D.IS()        


# # muliple
class class_room:
    def fct(self):
        print("teaching and research")
class lab:
    def fct1(self):
        print("only researcher")    
class clg(class_room,lab):
    def students(self):
        print("students are going both class room and lab") 
        
s=clg()
s.fct()
s.fct1()


                 