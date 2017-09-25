#import math
import math

#prints
print("In this calculator are different ways to choose, like calculating with kelvin and celsius or Pythagorean. You need to choose a number for the calculator that you want to use:")
print(" - Typ 1 for calculating with celsius and kelvin.")
print(" - Typ 2 for calculating with Pythagorean.")
print(" - Typ 3 for calculating with m/s and km/h.")
print(" - Typ 4 for calculating with a table.")
choose = int(input("Typ here your choose: "))

#KELVIN
if choose == 1:
	#Begin
	print("Do want to get from celsius to kelvin typ 1, do you want to get from kelvin to celsius typ 2.")
	kc = int(input("Typ here your choose (1/2): "))

	#Celsius to kelvin
	if kc == 1:
		kelvin = input("Typ here the celsius value: ")
		if kelvin.isdigit():
			celsiusans = int(kelvin) + 273
			print(celsiusans, 'Kelvin')
		else:
			print("That is not a digit.")
	#Kelvin to celsius
	elif kc == 2:
		celsius = input("Typ here the kelvin value: ")
		if celsius.isdigit():
			kelvinans = int(celsius) - 273
			print(kelvinans, 'Celsius')
		else: 
			print("That is not a digit.")
	#If the choose is not 1 or 2.
	else:
		print("You didn't choose 1 or 2.")

#PYTHAGOREAN
elif choose == 2:
	print("Do you want to know the tilt side typ 1, or the straight side typ 2.")
	pt = int(input("Typ here your choose (1/2): "))

	#tilt side
	if pt == 1:
		pythagorean = input("Typ one of your sides: ")
		pythagoreansecond = input("Typ the second side: ")
		if pythagorean.isdigit() and pythagoreansecond.isdigit():
			side = int(pythagorean) * int(pythagorean) + int(pythagoreansecond) * int(pythagoreansecond)
			tiltside = math.sqrt(side)
			print('Your tilt side is', tiltside)
		else: 
			print("That is not a digit.")
	#straight side
	if pt == 2:
		pythagoreanstraight = input("Typ the straight side: ")
		pythagoreanstraightsecond = input("Typ the tilt side: ")
		if pythagoreanstraight.isdigit() and pythagoreanstraightsecond.isdigit():
			sidestraight = int(pythagoreanstraight) * int(pythagoreanstraight)
			sidestraightsec = int(pythagoreanstraightsecond) * int(pythagoreanstraightsecond)
			straightside = sidestraightsec - sidestraight
			ansstraight = math.sqrt(straightside)
			print('Your straight side is', ansstraight)
		else:
			print("That is not a digit.")
#KM-M
elif choose == 3:
	print("Do you want to get from km/h to m/s (choose 1) or from m/s to km/h (choose 2)")
	km = int(input("Typ here your choose (1/2): "))

	#km/h to m/s
	if km == 1:
		kmtoms = input("Typ the km/h: ")
		if kmtoms.isdigit():
			kmans = int(kmtoms) / 3.6
			print(kmans, 'm/s')
		else:
			print("That is not a digit")
	elif km == 2:
		mstokm = input("Typ the m/s: ")
		if mstokm.isdigit():
			msans = int(mstokm) * 3.6
			print(msans, 'km/h')
		else:
			print("That is not a digit")
	else:
		print("You didn't choose 1 or 2.")

#TABLE
elif choose == 4:
	print("Enter the values in the sum. To get the unknown variable.")
	te = input("Typ the first value, of the table: ")
	te1 = input("Typ the second value, of the table: ")

	#sum
	if te.isdigit() and te1.isdigit():
		te2 = input("Typ the last value: ")
		sumans = int(te) * int(te1)
		te2sum = int(sumans) / int(te2)
		print(te2sum)
	else:
		print("You didn't enter a value.")
#ELSE
else:
	print("You didn't choose one of the options.")
