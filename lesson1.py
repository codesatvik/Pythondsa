print("hello world")
print("somthing")

print(20 + 19)
print(29)

print("Welcome to Python")
print("I will learn DSA")
print(100)
print(50)
print(15 + 10)

age = 10
name = "alex"

print(type(age))

x = "25"
y = int(x)

print(y + 5 ) #30

#name = input("Enter your name: ") #
#age = int(input("enter your age: ")) #
print("hello", name , "age" ,age)

print(10/3) #3.33
print(11//2) #5
print(11%2)# 1
print(2**3) #8

age = 13
if age > 18:
    print("you can vote")
else:
    print("you cannot vote")


z = 12
if z > 20:
    print("z is greater than 20")
elif z > 15:
    print("z is greater than 15")
elif z > 10:
    print("z is greater than 10")
else:
    print(z)

x = 8
if x > 5 and x < 10: # both 
    print("x is greater than 5 and less than 10")
else:
    print("x is not in the range")

if x < 5 or x == 8: # atleast one
    print("x is less than 5 or x is equal to 8")

if not x == 8:
    print("x is not equal to 8")
else:
    print("x is equal to 8")


for i in range(5):
    print(i)
# 1234

for i in range( 2, 10, 3):
    print(i)
# 2 5 8

i = 2
while i< 5:
    print(i)
    i += 1 
# 2 3 4 

print("range 1 to 6")
for i in range(1, 6):
    if i == 3:
        continue #ignore and move 
    if i == 5:
        break #stop at 4 
    print(i)
    
#1 2 4

def add(a,b):
    return a + b

x = add(3,1)
print(x) #4

