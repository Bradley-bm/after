num = int(input("Enter a whole number (base 10): "))
temp = num
binary = ""
if temp == 0:
    binary = "0"
else:
    while temp > 0:
        rem = temp % 2
        binary = str(rem) + binary
        temp = temp // 2
print("Binary number:", binary)
