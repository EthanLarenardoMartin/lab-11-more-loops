maximum_stories = 99;
floor = int(input("What floor do you work on? "));

while floor > maximum_stories:
    floor = int(input("You said " + str(floor) + ", but there are only "+ str(maximum_stories) +" floors in this building. What was the actual floor? "))
    print("Oh you work on floor " + str(floor) + " too? So do I!");