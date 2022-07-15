def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100,80)

if (balance <= 50):
    print("we need to make a deposit")  
else:
    print("nothing to see here!")

def function (name):
    print("hello,", name)

function("Alok")






#over 30 keywords only, return!


#line 6: open a space in ram and store the variable-> balance from the function withdraw_money(), using the parameters 100 current_balance, 80 amount)
#return the final value of the parameter: current_balance outside the withdraw_money() function and store it in the balance variable
#balance = 20, end line 6
#line 8-9, >>> "we need to make a deposit"


