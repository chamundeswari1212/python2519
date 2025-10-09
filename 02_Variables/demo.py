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
#print(x+a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


x,y,z=10,20,30
print(x+y+z)

