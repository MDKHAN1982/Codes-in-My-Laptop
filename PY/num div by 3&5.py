"""
1============================================================
x = int(input("Please enter a number:\n"))
if x % 3 == 0:
     if x % 5 == 0:
          print("Your number is divisible by 3 and 5 ")
     else:
          print("Your number is divisible by 3 and NOT 5.")
elif x % 5 ==0:
    print("Your number is divisible by 5 and NOT 3.")
else:
    print("Your number is NOT divisible by 3 and 5.")

2=============================================================
a=10
while a<1000:
    print(a)
    a=a+10
print("loop end")

3=========================================================
for x in "welcome to hellow world":
    print(x)

for x in [1,22,44,True,"welcome to hellow world"]:
    print(x)
4=========================================================
print("enter a and b values")
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print ("the number a is greatest:\n",a)
    if a==b or a==c:
          print("a and pther are equal:\n")   
elif b>=c and b>=a:

    print("the number b is greatest:\n",b)
    if b==c or b==a:
          print("b and other are equal:\n")
else:
    print("c is greatest")

5===================================================
from tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()

6============================================================
print("enter the value:\n")
a=int(input())
n=int(0)
while a>n:
    while a==n:
        print(n)
    n=n+1
=============================================================
"""
for x in range(0,10):
    for y in range (1,x+1):
        print(x,end='')
    print()
for x in range(0,10): 
    for y in range (1,11-x):
        print(x,end='')
    print()

