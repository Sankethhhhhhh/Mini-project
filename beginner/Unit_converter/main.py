def convert_length(value, from_unit, to_unit):
    conversions = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "inch": 0.0254,
        "foot": 0.3048
    }

    value_in_meters = value * conversions[from_unit]
    return value_in_meters / conversions[to_unit]


def convert_weight(value, from_unit, to_unit):
    conversions = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592
    }

    value_in_kg = value * conversions[from_unit]
    return value_in_kg / conversions[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "F":
        value = (value - 32) * 5/9
    elif from_unit == "K":
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == "F":
        return (value * 9/5) + 32
    elif to_unit == "K":
        return value + 273.15
    else:
        return value


def main():
    print("Unit Converter")
    print("Categories: length, weight, temperature")

    category = input("Enter category: ").lower()
    value = float(input("Enter value: "))
    from_unit = input("From unit: ")
    to_unit = input("To unit: ")

    if category == "length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        print("Invalid category")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()