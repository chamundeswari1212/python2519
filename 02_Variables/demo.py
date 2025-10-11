# working Variables
# Syntax --> var_name = value
# Syntax for text data is to enclose the text inside ' ' or " "
Student_name = 'Ravi'
Student_age = 20
Student_gpa = 9.5
Student_passed = True 


dynamic_var = 10
dynamic_var = 9.5
dynamic_var = False
dynamic_var = "Hello"
print(type(dynamic_var))
print(dynamic_var)

a=10
print(id(a)) #id() shows address of the variable

b=20
print(id(b))

c=10
print(id(c))


print("="*20)
#List means collection of multiple items --> list is represented using []
a_list = [10,20,30]
print(type(a_list))
print(a_list)
print(a_list[0])
print(a_list[-1])
print(id(a_list))

c_list=[10,20,30]
print(id(c_list))

x="python"
y="is"
z="awesome"
#output = python is awesome
#print(xyz) #NameError: name 'xyz' is not defined
print(x,y,z)
# + (add takes multiple numeric values and add them)
# + when used with numerics it's called as addition operator
# + when used with text it's called concatenation operator
# what is concatenation ? -> joining multiple strings
print(x+y+z) # joioning strings

# these method is called operator over loading one operator behaves/exbhits multiple behaviours based on the input data given(oops principle-polymorphism)

x=10
y=20
z=30
print(x+y+z) # adding numerics

a="10"
b="10"
#print(x+a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+b)

x,y,z=10,20,30
print(x+y+z)


s1,s2,s3 = "orange","apple","cherry"
print(s1+s2+s3)


print("="*20)
# using concatenation
name = "ravi"
age = 25
# print("My name is "+name +" and im "+age +"years old")
# TypeError: can only concatenate str (not "int") to str

# using interpolation
print(f"My name is {name} and im {age} years old")


print("="*20)
# using different values dynamically
x,y,z=10,20,30
age=25
print(f"Sum of x,y,z,age:{x+y+z+age}")


print("="*20)
# school student info
name = "john"
student_class = 8
student_school = "DPS"
print(f"My name is {name} is studying {student_class} class in {student_school} school")


print("="*20)
# key specifications of Mahindra Scorpio
ARAI_Mileage = "14.44 kmpl"
Engine_Displacement="2184 cc"
Max_Power="130bhp@3750rpm"
Seating_capacity=7.9
Boot_Space="460 Litres"
Body_Type="SUV"
print(f"key specifications of Mahindra Scorpio:ARAI_Mileage: {ARAI_Mileage} and Engine_Displacement: {Engine_Displacement} and Max_Power: {Max_Power} and Seating_capacity: {Seating_capacity} and Boot_Space: {Boot_Space} and Body_Type: {Body_Type}")

print("="*20)
# Operators

# Arithmetic Operator:
n1=3
n2=2
print(f"Sum of n1 and n2 is: {n1+n2}")
print(f"Difference of n1 and n2: {n1-n2}")
print(f"Product of n1 and n2: {n1*n2}")
print(f"Division of n1 and n2: {n1/n2}")
print(f"Modules of n1 and n2: {n1%n2}")
print(f"Floor Division of n1 and n2: {n1//n2}")
print(f"Exponentiation of n1 and n2: {n1**n2}")


print("="*20)
# Compound Assignment Operators
#without compound Assignment operator
x=10
x=x+5
print(x)
#with compound Assignment operator
x=10
x += 5
print(x)

print("="*20)
# Comparision Operators
n1=3
n2=2
print(n1==n2)

print("="*20)
# Logical Operators
x=7
y=5
a=5
b=9
resultand= a>y and a<b # T and F --> F
print(resultand)
resultor= a>y or a<b # T or F --> T
print(resultor)
resultnot= a>y or a<b # T or F --> T --> not (T) --> F
print(not resultnot)


print("="*20)
# Membership operators
a_list = [10,20,30]
is_present = 10 in a_list
print(is_present)
is_present = 100 in a_list
print(is_present)
is_present = 100 not in a_list
print(is_present)


data = "hello"
is_present = "l" in data
print(is_present)

print("="*20)
# Identity Operator
n1 = 10
n2 = 10
print(n1 is n2)
print(id(n1))
print(id(n2))

n1 = [10,20,30]
n2 = [10,20,30]
print(n1 is n2)
print(n1 == n2)
print(n1 is not n2)
print(id(n1))
print(id(n2))


print("="*40)
# Data Types
num = 10 # int
print(type(num))

num = 10.0 # float
print(type(num))

num = 1 + 2j #complex
print(type(num))

data = "hello" #string
print(type(data))

canVote = True # Boolean
print(type(canVote))

print("="*20)
# List
list_nums = [10,20,30]
print(type(list_nums))

# Tuples
tuple_nums = (10,20,30)
print(type(tuple_nums))

# Set
set_nums = {10,20,30,10,20,40}
print(type(set_nums))
print(set_nums)

# Dictionaries
Dict_nums = {'id':101,'name':'cham','age':21}
print(type(Dict_nums))
print(Dict_nums)

# None type
x = None
print(type(x))
print(x)

# Class
class Student: #class
    pass # Skip - do nothing
edify_Student = Student()
#object of these class edify_Student
print(type(edify_Student))


print("="*50)
# Student Management System
Student_id = 101
Student_Name = "John"
Student_Age = 20

# Scores
Quiz_score = 80
assignment_score = 75
exam_score = 90

#Attendence
Student_attendence = 60

#calculations
total_score = Quiz_score + assignment_score + exam_score
avg_score = total_score/3
student_passed = avg_score>75

#increement attendence
#student_attendence =student_attendence  + 1 #long hand
Student_attendence += 1 # short hand

# award eligibility
award_eligibility = Student_attendence >= 90 and student_passed

#process output
print("======= Student Report ==========")
print(f"Student Name: {Student_name}")
print(f"Student Total Score : {total_score}")
print(f"Student Average Score : {avg_score}")
print(f"Student Current Attendance : {Student_attendence}")
print(f"Student Passed : {student_passed}")
print(f"Student Awarded : {award_eligibility}")


