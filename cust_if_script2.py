#!/usr/bin/env python3

message = "Your network speed is "

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your network speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 85:
    message = message + 'on best speed performance.'
elif connection >= 60:
    message = message + 'on above average speed performance.'
elif connection >= 50:
    message = message + 'on average speed performance.'
else:
    message = message + 'slow. Try to contact your ISP..'
print(message)
