import random;

r = random.randint(1,100);

while(r):
    if r%2==0:
      print("The random number is even and the number is:",r);

    elif(r>=50 and r<=59):
        print("The number is between 50-59 and the number is:",r)
        continue;
    elif (r >= 96 and r <= 99):
        print("The number is between 96-99 and the number is:", r)
    break
