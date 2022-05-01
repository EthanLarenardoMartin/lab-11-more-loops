userstring = input("Gimme a number greater than 100. ")
usernum = int(userstring)

while usernum < 100: ## statement for when the termination is NOT true, keep the loop going...
## "While usernum is less than 100.."
    userstring = input(str(usernum) + " is less than 100, try something else! ")
    usernum = int(userstring)

print(str(usernum) + " is greater than 100, great job!")