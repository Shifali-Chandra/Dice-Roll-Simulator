import random
#to get a random no. from dice roll
import time
def input_choice():
    print("Type Start to roll a dice\nType End to exit")
    a=str(input())  
    return a
def logic(ch):
    if ch=='Start':
        print("*** Dice Rolling ***")
        #animation add krdo
        time.sleep(1)
        print(random.randint(1,6))
        logic(input_choice())
    elif ch=='End':
        pass 
    else:
        print('Incorret Choice\nEnter choice again')
        logic(input_choice())

      

