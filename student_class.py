#creating student class


class Student():
    #adding properties/atribute 
    name = ""
    age = 12 
    grade = "6th"
    teacher = "Mrs: Brown"

    #creating constructor function
    def __init__(self):
        print("making a new student")

    def change_details(self):
        print("please enter your age: ")
        self.age = int(input())
        print("please enter your name: ")
        self.name = input()

    def show_details(self):
        print("the details of the student are ")  
        print(self.age)
        print(self.name) 
        print(self.grade)
        print(self.teacher)

#creating objects/instances 

s1 = Student()
#to call a function from a class we need to write down - object_name.function:name
#calling the change detail function from the class 
s1.change_details()
#calling detail function from our class
s1.show_details()

#adding another object 

s2 = Student()
s2.change_details()
s2.show_details()

    









     

