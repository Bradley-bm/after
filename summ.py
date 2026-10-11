temperature = float(input("Enter the temperature in °C: "))
if temperature >= 25:
    print("It is warm! You can wear light and soft clothes.")
elif 18 <= temperature < 25:
    print("The weather is pleasant. A t-shirt or light shirt is good.")
else:
    print("It is too cold! Stick to your jacket and pullover.")
