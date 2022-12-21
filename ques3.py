a = int(input("Enter number: "))

b = int(input("Enter number: "))

c = int(input("Enter number: "))

if(a>b) and (a>c) : 
    greatest = a 
elif(b>a) and (b>c):
    greatest = b
else:
    greatest = c

print("The greatest number of all three is ", greatest)