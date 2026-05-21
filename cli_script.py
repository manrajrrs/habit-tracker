# This script greets the user and asks whether they have pushed any commits to Github

import csv 
from datetime import datetime

print('Good evening Manraj!')

while True:
    msg = input('Did you push to Git today? (Yes/No): ')

    if msg == 'Yes':
        print('Good work!')
        break
    
    if msg == 'No':
        print("That's ok, try again tomorrow!")
        break

    else:
        print('Try again!')

with open("file.txt", "a") as file:
    file.write(msg + ", " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + "\n")