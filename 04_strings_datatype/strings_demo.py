# Strings
s1="data"
s2='data'
s3='''data'''
s4="""data"""
print(s1,s2,s3,s4)
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))


# Multi line string
mls="""hi this is chaithanya 
recently graduated from annamacharya institute of technology and sciences"""
print(mls)


# ' inside a string
q= "how are you?"
# a='i'm fine' # SyntaxError: unterminated string literal (detected at line 21)
a="i'm fine"
print(a)
# a="doing"great"" # SyntaxError: invalid syntax
a='doing "great"'
print(a)

# Triple quotes
a='''i'm fine and doing "great"'''
print(a)
a="""i'm fine doing "great" """
print(a)

# Indexing 
s="python"
print(type(s))
print(s[1])
print(s[-1])

# print(text[10]) # IndexError: string index out of range
# print(text[-10]) # IndexError: string index out of range

# string accessing
text="python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

#using loops to access
print("using loops")
for i in text:
    print(i)

# len() (function)-> Return the number of items in a object
text="python " # space is also a character
print(len(text))
print("length is", len(text))
text="python"
print("length is", len(text))

# example using list
list_data = ["dell","lenovo","mac","acer","asus"]
print("Brands Count is", len(list_data))

# len() -> doesn't work with numbers
# num=100 # len() doesn't work with numbers/integers
# print(dir(num))
# print("Length is", len(num)) #TypeError: object of type 'int' has no len()


# Slicing in Python
text="python"
print(text[0]) # access using index

# [start:stop:step]
print(text[0:3]) # start : stop

print(text[0:6:2]) # start : stop : step

print(text[0:]) # start : end
print(text[:]) # total string will come
print(text[:4]) # start: stop
print(text[2:5]) # start : stop -->tho
print(text[:4]) # start(0) : stop(4) -->Pyth


print(text[-4:-1])
print(text[-1])
print(text[-4:])
print(text[:-1])
print(text[-6:-1:2])
# print(text[-4:-1:-1]) # empty 
print(text[-4:-6:-1]) # ty
# print(text[1:4:-1]) # empty
# reversing string
print(text[::-1])

#reversing text without slicing using logic
text="Python"
reverse_text=""
for i in text:
    reverse_text = i + reverse_text # adding each character to front yp
print("Reversed Text", reverse_text)

# Reassigning
text = "hello"
print(text)
text = "hi"
print(text)

# String Immutability
text = "hello"
print(text)

# Modify hello to Hello
# text[0]="H" 
# print(text) # TypeError: 'str' object does not support item assignment

# String Concatenation
s1= "Hello"
s2 = "Good Morning"
print(s1+s2)

# String Formatting
age = 30
# print("My age is "+age) # TypeError: can only concatenate str (not "int") to str
print("My Age is", age) 
print(f"My Age is {age}")
print("My Age is", +age)
print("My Age is "+str(age))

# String Repetition
text="Ha"
laugh="HaHaHaHa"
print(text)
print(laugh)
print("="*20)
laugh_hard=text*10
print(laugh_hard)


# String Methods
text = "Ha"
print(dir(text))

# simulate gmail functionality using strings
user_given_email = input("Enter your Email ID:")
format_email = user_given_email.lower()+"@gmail.com"
print("User Given ID:" +user_given_email)
print("Gmail Auto Format ID:" +format_email)


# simulate PAN correction -> https://www.pan.utiitsl.com/panonline_ipg/forms/ccsfPan.html/csfPreForm
user_given_pan=input("Enter Your PAN ID: ")
if user_given_pan.isalnum():
    format_pan = user_given_pan.upper()
    print("User Given PAN: "+user_given_pan)
    print("PAN Auto Format ID: "+format_pan)
else:
    print("User Given PAN is Invalid: "+user_given_pan)

# Functionality: check for sub string
# simulate email id verification -> name@gmail.com
user_given_email=input("Enter Your Email ID:")
if user_given_email.find("@") != -1:
    print("Valid Email")
else:
    print("InValid Email")
    
# Above can be achieved using operator also
user_given_email=input("Enter Your Email ID: ")
if "@" in user_given_email:
    print("Valid Email")
else:
    print("InValid Email")

# Redirect call based on given isd code
# https://usl.discourse-cdn.com/flex016/uploads/weweb/original/2x/d/dbeb05640347e2f7c1b7ae532ebb28f2.png
phone_number = input("enter your number with ISD Code: ")
if phone_number.startswith("+91"):
    print("call connected to INDIA")
elif phone_number.startswith("+86"):
    print("call connected to CHINA")
elif phone_number.startswith("+33"):
    print("call connected to FRANCE")
else:
    print("ISD Available Only To INDIA, CHINA & FRANCE")
    
# Check if email synchronization is possible are not
source_email = input("enter your source email id: ")
destination_email = input("enter your destination email id:")
if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("synchronizing")
else:
    print("Both Emails should be from same providers")

# simulate gmail functionality -> remove spaces from input
user_given_email=input("enter your email id: ")
format_email=user_given_email.strip()
print("User Given ID: "+user_given_email)
print("Gmail Auto Format ID: "+format_email)

# Read Data From CSV File

# sample data taken from a CSV file
# "Name, City, Age, Email, Role"
csv_line= "John,Hyd,john@gmail.com,developer"


# Original Data 
print("Original Line: "+csv_line)

parsed_fields = csv_line.split(",")
print("Parsed Data: ",parsed_fields)

# Access Name & Role
print("Name: ",parsed_fields[0])
print("Role: ",parsed_fields[4])

# VS Code Find & Replace / OTP template / Order ID Template
email_template = "Hello User, Your order #{order_id} hass been shipped"
#username = "john"
order_id = "OD-ID-9090"

# Replacing place holder with values
# personlized_email = email_template.replace("{username}",username)
personlized_email=email_template.replace("{order_id},order_id")

# Sending email
print(personlized_email)

