x = int(input("enter number for x: "))
y = int(input("enter number for y: "))

print('this will be printed because it is above error')
result = x / y

print(f"result {result}")
try:
    result - x / y
    print(f"result {result}")
except ZeroDivisionError:
    print("cannot divide by zero")

print("this will be printed")

b = 10
a = 5

if b == 0:
    raise ZeroDivisionError("Cannot!")

print(a/b)