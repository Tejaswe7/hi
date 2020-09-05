#LCM of two numbers

x=float(input("enter first number:"))
y=float(input("enter second number:"))

#logic begins here
if (x>y):
  greater=x
else:
    greater=y
    while(true):
if ((greater % x == 0) and (greater % y == 0)):
  lcm = greater
  break
  greater += 1
  #display result
  print("the LCM is",lcm)


  