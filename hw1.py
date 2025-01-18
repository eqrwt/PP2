#2nd problem
import sys

print(sys.version)

# here 1st assignment  
print("Hello world")

#here example using variable and input from terminal
n = int(input())

#here another example of using if
if n > 2:
    print("No there other people here")
if n == 2:
    print("Just the two of us")


#here good example of using global and other things in working with variables
x = "awesome"

def myfunc():
  x = "fantastic"
myfunc()
print("Python is " + x)

# here adding global keyword to show how we can change x
x = "awesome"

def myfunc():
  global x  
  x = "fantastic"
myfunc()
print("Python is " + x)


