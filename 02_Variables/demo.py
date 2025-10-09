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

# using concatenation
name = "ravi"
age = 25
# print("My name is "+name +" and im "+age +"years old")
# TypeError: can only concatenate str (not "int") to str

# using interpolation
print(f"My name is {name} and im {age} years old")

# using different values dynamically
x,y,z=10,20,30
age=25
print(f"Sum of x,y,z,age:{x+y+z+age}")


# school student info
name = "john"
student_class = 8
student_school = "DPS"
print(f"My name is {name} is studying {student_class} class in {student_school} school")


# key specifications of Mahindra Scorpio
ARAI_Mileage = "14.44 kmpl"
Engine_Displacement="2184 cc"
Max_Power="130bhp@3750rpm"
Seating_capacity=7.9
Boot_Space="460 Litres"
Body_Type="SUV"
print(f"key specifications of Mahindra Scorpio:ARAI_Mileage: {ARAI_Mileage} and Engine_Displacement: {Engine_Displacement} and Max_Power: {Max_Power} and Seating_capacity: {Seating_capacity} and Boot_Space: {Boot_Space} and Body_Type: {Body_Type}")
