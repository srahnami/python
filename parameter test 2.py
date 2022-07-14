def dark_magician(mode):
	if mode == "attack":
		print("dark magic attack")
	if mode == "defense":
		print("in defense mode")
'''	
	if mode != "attack" or "defense":
		print("aha this is not either one!")
'''



x = (input("attack or defense \n"))
dark_magician(x)

#computer only uses this once then throws it away
'''
if input != "attack": #or "defense" or "hi": 
	#Oh, input is used in the same line the computer asks for it--
	print("try again \n")
	dark_magician(input("attack or defense \n"))
'''


if input("attck now") == "attack":
	dark_magician("attack")

if input("defend, now!") == "defend":
	dark_magician("defense")

if input("do something else!") != "attack" or "defense":
	dark_magician("dunno")

#if you want to use the user's input again you have to store in a variable

#learned how to use input; line 18 doesn't do what i intend it to b/c ur asking input to have a value without using the function properly(use input())
#("input is single-use, disposable. useless on its own just typing input()" it's like talking to a wall...?)
