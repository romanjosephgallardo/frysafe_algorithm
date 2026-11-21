
import json
from pathlib import Path


# Locate the project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Calibration file location
CALIBRATION_FILE = BASE_DIR / "calibration" / "calibration.json"


def load_calibration():
    """
    Load baseline and maximum reference values
    from the calibration JSON file.
    """

    if not CALIBRATION_FILE.exists():
        raise FileNotFoundError(
            f"Calibration file not found: {CALIBRATION_FILE}"
        )

    with open(CALIBRATION_FILE, "r") as file:
        calibration = json.load(file)

    return calibration


def normalize_value(value, baseline, maximum):
    """
    Normalize a sensor reading using the calibration references.

    Formula:
        N = (X - baseline) / (maximum - baseline)

    The result is restricted to the range 0 to 1.
    """

    denominator = maximum - baseline

    if denominator == 0:
        raise ValueError(
            "Invalid calibration: baseline and maximum are equal."
        )

    normalized = (value - baseline) / denominator

    # Keep normalized values within 0 to 1
    normalized = max(0.0, min(1.0, normalized))

    return normalized


def normalize_readings(readings):
    """
    Normalize all four FrySafe sensor readings.

    Expected input:
        {
            "red": value,
            "green": value,
            "blue": value,
            "turbidity": value
        }
    """

    calibration = load_calibration()

    baseline = calibration["baseline"]
    maximum = calibration["maximum"]

    normalized_readings = {}

    for sensor in ["red", "green", "blue", "turbidity"]:

        if sensor not in readings:
            raise ValueError(f"Missing sensor reading: {sensor}")

        if sensor not in baseline or sensor not in maximum:
            raise ValueError(f"Missing calibration reference: {sensor}")

        normalized_readings[sensor] = normalize_value(
            value=float(readings[sensor]),
            baseline=float(baseline[sensor]),
            maximum=float(maximum[sensor])
        )

    return normalized_readings


if __name__ == "__main__":

    # Example sensor readings for testing only
    sample_readings = {
        "red": 850,
        "green": 750,
        "blue": 650,
        "turbidity": 2500
    }

    results = normalize_readings(sample_readings)

    print("\nFrySafe Normalization Results")
    print("-----------------------------")

    for sensor, value in results.items():
        print(f"{sensor.capitalize()}: {value:.4f}")
