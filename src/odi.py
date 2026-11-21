
import math


REQUIRED_SENSORS = ["red", "green", "blue", "turbidity"]


def compute_odi(normalized_readings):
    """
    Compute the FrySafe Oil Degradation Index (ODI).

    Formula:
        ODI = ((NR + NG + NB + NT) / 4) * 100

    Returns:
        float: ODI value between 0.0 and 100.0.
    """

    values = []

    for sensor in REQUIRED_SENSORS:

        if sensor not in normalized_readings:
            raise ValueError(
                f"Missing normalized reading: {sensor}"
            )

        value = float(normalized_readings[sensor])

        if not math.isfinite(value):
            raise ValueError(
                f"Invalid normalized value for {sensor}: {value}"
            )

        if not 0.0 <= value <= 1.0:
            raise ValueError(
                f"Normalized value for {sensor} must be between 0 and 1."
            )

        values.append(value)

    odi = (sum(values) / len(values)) * 100

    return odi


if __name__ == "__main__":

    # Sample normalized readings for software testing only
    sample_normalized_readings = {
        "red": 0.50,
        "green": 0.45,
        "blue": 0.55,
        "turbidity": 0.60
    }

    result = compute_odi(sample_normalized_readings)

    print("\nFRYSAFE ODI COMPUTATION")
    print("--------------------------------")

    for sensor, value in sample_normalized_readings.items():
        print(f"Normalized {sensor.capitalize()}: {value:.4f}")

    print("--------------------------------")
    print(f"Oil Degradation Index: {result:.2f}")
