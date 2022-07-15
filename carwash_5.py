

def car_wash(amount_paid):
    if (amount_paid >= 12):
        print("Tricolor foam")
        print("two rinses")
        print("Blow dry")
        print("your change is $", amount_paid - 12)


    if (amount_paid >= 6):  
        print("white foam")
        print("one rinse")
        print("drip dry")  
        print("your change is $", amount_paid - 6)
    else:
        print("gib more money \n")
        print("machine spits out the money in your face \n")
        print("you feel sadness")
        car_wash(int(input("how much now loser \n")))

car_wash(int(input("how much \n")))

print("have a nice day!")

car_wash(int(input("how much \n")))


#"how much" - > user inputs (line 22
# if greater than or equal to 12; premium and change (does not accept small change)
#user input is limited by int going through -- terminal will output error if the value is not convertable to int, "str" or floats
# greater than or equal to 6; basic wash plus, "your change is $ amount_paid aka user input minus 6 math"
# if less than 6; "gib more money, machine..., you feel..., then finally, "how much now loser \n"
#
# car_wash can be called as few as 2 times and as many as 3 times (if you don't put enough money in) 

#3 ways to improve
#accept/don't accept cent amt (error)
#int-only user-input plz
#if string or float... then.. invalid
#a smart aleck robot, or a simple machine
#simple prob also means less breakable but
#more limited and boring for the user
#but straightforward
#not many ways to kill it if used built-in
#tools correctly.


x = int(input("put age"))
def age():
    print("you are", x,"years old")

age(x)
