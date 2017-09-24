print("Wil je kelvin krijgen of celsius? Typ 1 voor het omzetten van celsius naar kelvin, 2 voor het omzetten van kelvin naar celsius.")
kc = int(input("Typ hier je keuze: "))

#Omzetten celsius naar kelvin
if kc == 1:
	kelvin = input("Typ hier het aantal graden: ")
	if kelvin.isdigit():
		celsiusans = int(kelvin) + 273
		print(celsiusans)
	else:
		print("Dat is geen cijfer.")
#Omzetten kelvin naar celsius
elif kc == 2:
	celsius = input("Typ hier het aantal kelvin: ")
	if celsius.isdigit():
		kelvinans = int(celsius) - 273
		print(kelvinans)
	else: 
		print("Dat is geen cijfer.")
#Als de keuze geen 1 of 2 is
else:
	print("Je koos geen 1 of 2.")