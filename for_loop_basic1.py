# prints all integers from 0 to 150
for x in range(0,151):
    print(x)

#prints all the multiples of 5 from 5 to 1,000
for x in range(5,1005,+5):
    print(x)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101):
    if x % 10 == 0:
        print("Coding")
    elif x % 5 == 0:
        print("Coding Dojo")
    else:
        print(x)

#Add odd integers from 0 to 500,000, and print the final sum
total = 0
for x in range(1,500000,+2):
    total += x
print(total)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    print(x)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)