#strings
print("Hello World")

#numbers
print(123)

#expressions
print(123 + 456)

#variables
my_variable = "Hello World"
print(my_variable)

#print multiple items
name = "Dev"
age = 23
print("Hello my name is " + name + " and I am ", age ,"years old.")

#controlling separator
print("Hello","My","Name","Is","Dev", sep="-")

#controlling ending Of the print statement by default it is \n means a new line but if we want to change it we can use the end parameter
print("Hello world my name is dev", end="...")

print("Hello" , end=" ")
print("World")

#escape characters
print("Hello \n world")#new line
print("Hello \t world")#tab space
print("Hello \\ world")#backslash
print("Hello \' world")#single quote
print("Hello \" world")#double quote

#formartted strings
name = "Dev"
age = 23
print(f"Hello my name is {name} and I am {age} years old.")
print("Hello my name is",name,"and I am",age,"years old.")

print("My name is {}, age {}".format(name, age))
print("My name is %s, age %d" % (name, age))

#print with expressions

x,y,z = 1,2,3

print("Addition = ", x+y+z)
print("Multiply = ", x*y*z)

a = "Python"
print(a)

print("Smiley:", "\U0001F600")   # 😀
print("Heart:", "\u2764")        # ❤