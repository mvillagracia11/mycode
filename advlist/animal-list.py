#!/usr/bin/env python3

def main():

    # create a list called list1
    list1 = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]
    list2 = ["Eel", "Bug", "Cow", "Dib"]
    list3 = ["Pet"]

    print(list1[7])
    print(list1[3:6])

    list1.append(list2)
    print(list1)

    list2.extend(list3)
    print(list2)

main()
