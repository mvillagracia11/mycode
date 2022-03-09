# https://github.com/csfeeser/Python/blob/master/challenges/Busted%20Code%20Morning%20Review.md

#!/usr/bin/env python3  # missing /bin


def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True: # true should be True
        name= input("What is your name?\n>") # missing quotes ""
        num= int(input("Pick a number between 1 and 3: "))
        
        if num in words.keys(): # name is not needed
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")  # missing () after capitalize
            break    # typo was brake
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!

main()   # this was missing
