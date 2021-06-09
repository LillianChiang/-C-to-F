question = input('What temperature would you like to convert? 1.Celsius, 2.Fahrenheit: ')
question = int(question)

if question == 1:
    Celsius = input('Enter Celsius: ')
    Celsius = float(Celsius)
    result = Celsius*9/5+32
    print('Fahrenheit is ',result, '°F')
else:
    Fahrenheit = input('Enter Fahrenheit: ')
    Fahrenheit = float(Fahrenheit)
    result2 = (Fahrenheit-32)*5/9
    print('Celsius is :', result2, '°C')








