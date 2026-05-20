# This script greets the user and asks whether they have pushed any commits to Github

print('Good evening Manraj!')

while True:
    msg_1 = input('Did you push to Git today? (Yes/No): ')

    if msg_1 == 'Yes':
        print('Good work!')
        break
    
    if msg_1 == 'No':
        print("That's ok, try again tomorrow!")
        break

    else:
        print('Try again!')