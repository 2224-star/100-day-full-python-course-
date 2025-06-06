## Create a python program capable of greeting you with good 
# morning good afternoon and good evning your program should use time module
# to get the current hour hare is a sample 
# program and documentation

import time

current_time = time.localtime().tm_hour

if 5<= current_time < 12:
    print("Good Morning!")
elif 12 <= current_time < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")
    # This code checks the current hour and prints a greating 
    # based on the time of day.

    