temperature = eval(input("Enter the temperature in Fahrebheit between -58 and 41:"))
WindSpeed = eval(input("Enter the wind speed in  miles per hour:"))
Wind_chill_index = 35.74 + 0.6215*temperature - 35.75*(WindSpeed**0.16) + 0.4275*temperature*(WindSpeed**0.16)
print("The wind chill index is :",format(Wind_chill_index,"2.5f"))