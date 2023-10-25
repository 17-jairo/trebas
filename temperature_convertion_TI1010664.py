def fahrenheit_to_celsius_and_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    return celsius, kelvin


def celsius_to_fahrenheit_and_kelvin(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin


def kelvin_to_celsius_and_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    return celsius, fahrenheit


def temp_convert():
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the temperature unit (K / C / F): ").upper()

        conversions = {'F': fahrenheit_to_celsius_and_kelvin, 'C': celsius_to_fahrenheit_and_kelvin, 'K': kelvin_to_celsius_and_fahrenheit}

        if unit in conversions:
            converted_values = conversions[unit](temp)
            if unit == 'F':
                print(f"{temp} Fahrenheit is equivalent to {converted_values[0]:.2f} Celsius and {converted_values[1]:.2f} Kelvin.")
            elif unit == 'C':
                print(f"{temp} Celsius is equivalent to {converted_values[0]:.2f} Fahrenheit and {converted_values[1]:.2f} Kelvin.")
            else:
                print(f"{temp} Kelvin is equivalent to {converted_values[0]:.2f} Celsius and {converted_values[1]:.2f} Fahrenheit.")
        else:
            print("Invalid temperature unit. Must be F, C, or K.")
    except ValueError:
        print("Please enter a valid number for the temperature.")


if __name__ == "__main__":
    temp_convert()
