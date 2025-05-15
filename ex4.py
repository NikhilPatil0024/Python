# Greetings.

import time

currentHour = int(time.strftime("%H"))

if 4 <= currentHour < 12:
    print("Good Morning!")

elif  12 <= currentHour < 17:
    print("Good Afternoon!")

elif 17 <= currentHour < 19:
    print("Good Evening!")

else: 
    print("Good Night!")

print(currentHour)
