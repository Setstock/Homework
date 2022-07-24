N=int(input('How many stricks in the pile:'))
print("There are",N,"sticks in the pile.")
name=str(input("What is yor name:"))
count = 0
while (N != 0):
  x=int(input(name+",how many sticks you will take (1 or 2):"))
  if (x>2):
    print("No you cannot take more than 2 sticks!")
  elif (x<1):
    print("No you cannot take more less than 1 stick!")
  elif (x>N):
    print("There are no enough sticks to take.")
  else:
    count += 1
    N=N-x
    if (N != 0): 
      print("There are",N,"sticks in the pile.")
    else:
       print("OK. There is no stick left in the pile. You spent",count,"times.")