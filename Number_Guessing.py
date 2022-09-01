import random
import numpy as np
k=np.random.randint(1,100)
print("GUESS the number:")
l=['num lie between 1 to 100']
if(k%2==0):
    l.append('num is multiple of 2')
else:
    l.append('num is odd')
for i in range(3,9):
    if(k%i==0):
        l.append('num is divisible by %d'%i)
def guess(x):
    if(x==k):
     print('congrats')
    else:
      print("wrong answer try again")
      for j in l:
        print(j)
        del l[l.index(j)]
        break
      guess(int(input())) 
guess(int(input()))