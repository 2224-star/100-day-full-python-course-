### Create a python program capable of greting you with good morning , good afternon and good Evning your program should use tiem module to get the current hour here is a sample program and documentation link for you
 
import time
current_hour = time.localtime().tm_hour
if current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 17:
    print("Good Afternoon")
elif 17 <= current_hour < 21:
    print("Good Evening")
else:
    print("Hello It's late, take rest!")