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

# identyfing variables type here how

haski = set((1, 2, 2, 3))
print(type(haski))


# playing with type of numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

