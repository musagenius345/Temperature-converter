'''This is a temperature converter that convert to and fro Celsius, Kelvin and Fahrenheit '''
print('Temperature converter\nEnter the following entries to choose what you want to convert')
print('1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit\n3.Celsius to Kelvin\n4.Kelvin to Fahrenheit\n5.Fahrenheit to Kelvin\n6.Kelvin to Celsius')
print("Press space or enter 'OK' to end converter")
trial = 0
for i in range(10):
	conv1 = int(input('Entry: ')) 
	if conv1 == 1:
		print('Converting Fahrenheit to Celsius')
		print('Input the Fahrenheit degree: ')
		F = float(input(''))
		C = (F - 32)*(5/9)
		print(round(C, 2), '°C')
	elif conv1 == 2:
		print('Converting Celsius to Fahrenheit')
		print('Input the Fahrenheit degree: ')
		C = float(input(''))
		F = 1.8*C + 32
		print(round(F, 2), '°F')
	elif conv1 == 3:
		print('Converting Celsius to Kelvin')
		print('Input the Celsius degree: ')
		C = float(input(''))
		K = (C + 273.15)
		print(round(K, 1), 'K')
	elif conv1 == 4:
		print('Converting Kelvin to Fahrenheit')
		print('Input the Celsius degree: ')
		K = float(input(''))
		C = (K - 273.15)
		F = 1.8*C + 32
		print(round(F, 2), '° F')
	elif conv1 == 5:
		print('Converting Fahrenheit to Kelvin')
		print('Input the Fahrenheit degree: ')
		F = float(input(''))
		C = (F - 32)*(5/9)
		K = (C + 273.15)
		print(round(K, 1), 'K')
	elif conv1 == 6:
		print('Converting Kelvin to Celsius')
		print('Input the Kelvin: ')
		K = float(input(''))
		C = (K - 273.15)
		print(round(C, 2), '°C')
	else:
		print('Invalid Error')
		trial += 1
		while trial > 5:
			print('Thank you for using this program')
			break
	

	