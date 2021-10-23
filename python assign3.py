import sys
import datetime;
# print the string
ST= "Twinkle Twinkle little star \n \t How are wonder what your are! \n\t Up above the world so high \n Like a diamond in the sky. ";
print (ST);
#Write a Python program to get the Python version you are using
print("python version---"); 
print(sys.version);
#Write a Python program to display the current date and time.
print(datetime.datetime.now());
"""Write a Python program which accepts the radius of a circle from the user and compute
the area"""
radius=float(input("Enter radiuus of circle: "));
area=round(3.14*radius*radius);
print("Area of cirlce is: ");
print(area);
"""Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them."""
first=input("Enter firstname: ");
last=input("Enter lastname: ");
print(last+" "+first);
# Write a python program which takes two inputs from user and print them addition
a=int(input("Enter one integer: "));
b=int(input("Enter second integer: "));
print(a+b);
"""Write a program which take input from user and identify that the given number is even
or odd?"""
num=int(input("Enter number:"));
if(num%2==0):
    print("number is even");
else:
  print("number is odd");  
#Write a program which print the length of the list?
a=[2,3,4,14,6,7,8];
print(len(a));
#.Write a Python program to sum all the numeric items in a list?
sum1=0;
for i in range(0,len(a)):
    sum1+=a[i]
print(sum1);  
#Write a Python program to get the largest number from a numeric list.
max=a[0];
for i in range(0,len(a)):
    if(max<a[i]):
        max=a[i];
print(max); 
"""Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Write a program that prints out all the elements of the list that are less than 5."""
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
for i in range(0,len(a)):
    if(arr[i]<5):
        print(arr[i]); 
        
        