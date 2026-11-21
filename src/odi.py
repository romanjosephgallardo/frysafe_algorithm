
def compute_odi(normalized_readings):
    """
    Calculate the FrySafe Oil Degradation Index (ODI).

    Formula:
        ODI = ((NR + NG + NB + NT) / 4) * 100

    Parameters:
        normalized_readings (dict):
            {
                "red": normalized red frequency,
                "green": normalized green frequency,
                "blue": normalized blue frequency,
                "turbidity": normalized turbidity voltage
            }

    Returns:
        float: Oil Degradation Index (0 to 100).
    """

    required_sensors = ["red", "green", "blue", "turbidity"]

    # Check if all required sensor values are present
    for sensor in required_sensors:
        if sensor not in normalized_readings:
            raise ValueError(f"Missing normalized reading: {sensor}")

    # Retrieve and validate normalized values
    values = []

    for sensor in required_sensors:
        value = float(normalized_readings[sensor])

        if not 0.0 <= value <= 1.0:
            raise ValueError(
                f"Invalid normalized value for {sensor}: {value}. "
                "Expected a value between 0 and 1."
            )

        values.append(value)

    # Calculate the arithmetic mean and convert to a percentage
    odi = (sum(values) / len(values)) * 100

    return odi


if __name__ == "__main__":

    # Sample normalized readings for testing only
    sample_normalized_readings = {
        "red": 0.50,
        "green": 0.45,
        "blue": 0.55,
        "turbidity": 0.60
    }

    result = compute_odi(sample_normalized_readings)

    print("\nFrySafe ODI Computation")
    print("-----------------------")

    for sensor, value in sample_normalized_readings.items():
        print(f"Normalized {sensor.capitalize()}: {value:.4f}")

    print("-----------------------")
    print(f"Oil Degradation Index (ODI): {result:.2f}")
