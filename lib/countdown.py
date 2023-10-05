# your code goes here!
import time

def countdown(i):
    
    while i:
        print(f"{i} SECOND(S)!")
        i -= 1
    print("HAPPY NEW YEAR!")
        

def countdown_with_sleep(number):
    
    while number:
        print(f"{number} SECOND(S)!")
        number -= 1
        time.sleep(1)

    print("HAPPY NEW YEAR!")

countdown_with_sleep(10)