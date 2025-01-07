"""conversion of temperature from celsius to fahrenheit."""


def celsius_to_fahrenheit(celsius_list):
    """
    Convert a list of temperatures from Celsius to Fahrenheit.

    Args:
        celsius_list (list): List of temperatures in Celsius.

    Returns:
        list: List of temperatures converted to Fahrenheit.

    Raises:
        ValueError: If input is not a list or contains invalid elements.
    """
    if not isinstance(celsius_list, list):
        raise ValueError("Input must be a list.")

    fahrenheit_list = []

    for temp in celsius_list:
        if not isinstance(temp, (int, float)):
            raise ValueError("List elements must be integers or floats.")

        fahrenheit = (9 / 5) * temp + 32
        fahrenheit_list.append(round(fahrenheit, 2))

    return fahrenheit_list


if __name__ == "__main__":
    user_input = input("Enter the temperature in celsius: ")

    input_celsius_list = []
    if not user_input.strip():
        print("Error: No input provided.")
    else:
        try:
            input_celsius_list = [float(temp.strip()) for temp in user_input.split(",")]
        except ValueError:
            print(
                "Error: Invalid input. Please enter a list of numbers separated by commas."
            )
            input_celsius_list = []

    try:
        result = celsius_to_fahrenheit(input_celsius_list)
        print("The list of temperature in fahrenheit is:", result)
    except ValueError as e:
        print("Error:", e)
